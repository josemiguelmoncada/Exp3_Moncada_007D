from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'productos/', views.productos, name='productos'),
    path(r'sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path(r'registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path(r'login/', views.login_personalizado, name='login'),
    path(r'logout/', views.cerrar, name="cerrar"),
    path(r'panel_admin/', views.panel_admin, name='panel_admin'),
    path(r'producto/#<id>', views.detalle_Producto, name='producto'),
    path(r'crearProducto/', views.crearProducto, name='crearProducto'),
    path(r'modificarProducto/#<id>', views.modificarProducto, name='modificarProducto'),
    path(r'eliminarProducto/#<id>', views.eliminarProducto, name='eliminarProducto'),
    path(r'crear_tipo/', views.crear_tipo, name='crear_tipo'),
    path(r'eliminar_tipo/#<id>', views.eliminar_tipo, name='eliminar_tipo'),
    path('ver-perfil/', views.ver_perfil, name='ver_perfil'),
    path('actualizar_email/', views.actualizar_email, name='actualizar_email'),
    
    path('carrito/', views.ver_carrito, name='carrito'),
    path('agregar/<id>', views.agregar_producto, name='agregar'),
    path('agregar_/<id>', views.agregar_producto1, name='agregar1'),
    path('eliminar/<id>', views.eliminar_producto, name='eliminar'),
    path('restar/<id>', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),

]