from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Tipo_producto, Boleta, DetalleBoleta
from .forms import ProductoForm, TipoForm, RegistroUsuarioForm, BuscarProductoForm
from rest_framework import generics
from .serializers import ProductoSerializer
from Tienda.compras import Carrito
import os
import json
from django.conf import settings
from django.http import JsonResponse
import locale


# Create your views here.
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

def formatear_pesos_chilenos(valor):
    return locale.currency(valor, symbol=True, grouping=True)



class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def mostrar_productos(request):
    return render(request, 'productos.html')

def exportarJSON(request):
    productos = Producto.objects.all().values()
    productos_list = list(productos)
    file_path = os.path.join(settings.MEDIA_ROOT, 'productos.json')
    with open(file_path, 'w') as json_file:
        json.dump(productos_list, json_file)
    
    return redirect('panel_admin')
    # return JsonResponse({'message': 'Productos exportados correctamente', 
    #                      'file_path': settings.MEDIA_URL + 'productos.json'})







def index(request):
    productos = Producto.objects.order_by('precio')[:4]
    
    for producto in productos:
        producto.precio  =  formatear_pesos_chilenos(producto.precio)
        
    context = {
        'productos': productos
    }

    return render(request, 'index.html', context)

def productos(request):
    producto = Producto.objects.all()
    
    for product in producto:
        product.precio  =  formatear_pesos_chilenos(product.precio)
        
    context = {"producto":producto}
    return render(request, 'productos.html', context)

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def buscar_productos(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        resultados = Producto.objects.filter(nombre__icontains=query)
        productos = [
            {
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'imagen': producto.imagen.url if producto.imagen else '',
                'id_producto': producto.id_producto,
                'url': f'/producto/{producto.id_producto}'
            }
            for producto in resultados
        ]
        return JsonResponse({'resultados': productos})
    
    form = BuscarProductoForm()
    return render(request, 'buscar_productos.html', {'form': form})


@login_required
def panel_admin(request):
    producto = Producto.objects.all()
    tipo = Tipo_producto.objects.all()
    context = {"producto":producto,
               "tipo":tipo}
    return render(request, 'panel_admin.html', context)

# i CRUD Productos
def detalle_Producto(request, id):
    carrito_compra = Carrito(request)
    producto = get_object_or_404(Producto, id_producto=id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))  # Obtener cantidad del formulario
        carrito_compra.agregar(producto=producto, cantidad=cantidad)

    context = {"producto": producto}
    return render(request, "producto_card.html", context)

def crearProducto(request):
    if request.method == 'POST':
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect('panel_admin')
    else:
        productoform = ProductoForm()
    return render(request, 'Crud_Productos/crear.html', {'Productoform':productoform})

def modificarProducto(request, id):
    producto = Producto.objects.get(id_producto = id)
    datos = {
        'formModificar': ProductoForm(instance=producto),
        'producto':producto
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('panel_admin')
    return render(request, 'Crud_Productos/modificar.html', datos)

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id_producto = id)
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            producto.delete()
            return redirect('panel_admin')
    return render(request, 'Crud_Productos/eliminar.html', {"producto":producto})
# e CRUD Productos

# i CRUD Tipo
def crear_tipo(request):
    if request.method == 'POST':
        tipoform = TipoForm(request.POST, request.FILES)
        if tipoform.is_valid():
            tipoform.save()
            return redirect('panel_admin')
    else:
        tipoform =TipoForm()
    return render(request, 'Crud_Tipo/crear.html', {'Tipoform':tipoform})

def eliminar_tipo(request, id):
    tipo = get_object_or_404(Tipo_producto, id_tipo=id)
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            tipo.delete()
            return redirect('panel_admin')
    return render(request, 'Crud_Tipo/eliminar.html', {'tipo':tipo})

# e CRUD Tipo

# i usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =RegistroUsuarioForm()
    return render(request, 'registro_usu.html', {'form':form})

def login_personalizado(request):
    if request.method == 'POST':
        data = request.POST
        form = AuthenticationForm(request, data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Error en el formulario de autenticación')
    else:
        form = AuthenticationForm()
    
    return render(request, 'header_ul1.html', {'form': form})

@login_required
def ver_perfil(request):
    usuario = request.user
    
    context = {
        'usuario': usuario
    }
    return render(request, 'perfil.html', context)

@login_required
def actualizar_email(request):
    if request.method == 'POST':
        nuevo_email = request.POST.get('email')
        usuario = request.user
        usuario.email = nuevo_email
        usuario.save()
        messages.success(request, 'Correo electrónico actualizado con éxito')
        return redirect('ver_perfil')  # Redirige a la página de perfil o cualquier otra página

    return render(request, 'perfil.html')

def cerrar(request):
    logout(request)
    return redirect('index')

# e usuario

def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id_producto = id)
    carrito_compra.agregar(producto=producto)
    return redirect('producto')  

def agregar_producto1(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id_producto = id)
    carrito_compra.agregar(producto=producto, cantidad=1)
    return redirect('carrito')  

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(id_producto = id)
    carrito_compra.eliminar(producto=producto)
    return redirect('cart/view_cart.html')  

def restar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = get_object_or_404(Producto, id_producto=id)
    carrito_compra.restar(producto=producto)
    return redirect('carrito') 

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('carrito')


def ver_carrito(request):

    
    carrito_compra = Carrito(request)
    subtotal = carrito_compra.obtener_subtotal()
    subtotal_iva = carrito_compra.obtener_subtotal_iva()
    total = carrito_compra.obtener_total()
    context = {
        'carrito': carrito_compra.carrito,
        'subtotal': formatear_pesos_chilenos(subtotal),
        'subtotal_iva': formatear_pesos_chilenos(subtotal_iva),
        'total': formatear_pesos_chilenos(total),
    }
    return render(request, 'cart/view_cart.html', context)

@login_required
def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(id_producto = value['id_producto'])
            cant = value['cantidad']
            producto.stock -= cant # reducir el stock total segun la cantidad que se compro
            subtotal = cant * int(value['precio'])
            s_iva = round(subtotal * 0.19)
            detalle = DetalleBoleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            producto.save()
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': formatear_pesos_chilenos(round(boleta.total+s_iva)),
        'subtotal_iva': formatear_pesos_chilenos(s_iva),
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)


