class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito
        
    def agregar(self, producto, cantidad):
        producto_id = str(producto.id_producto)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                "id_producto": producto.id_producto,
                "nombre": producto.nombre,
                "precio": int(producto.precio),
                "imagen": producto.imagen.url,
                "cantidad": cantidad,
                "total": producto.precio * cantidad,
            }
        else:
            nueva_cantidad = self.carrito[producto_id]["cantidad"] + cantidad
            
            # Verificar nuevamente el stock disponible
            if producto.stock < nueva_cantidad:
                self.carrito[producto_id]["cantidad"] = producto.stock
            else:
                self.carrito[producto_id]["cantidad"] += cantidad
                self.carrito[producto_id]["total"] += producto.precio * cantidad
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        producto_id = int(producto.id_producto)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()
    
    def restar(self, producto):
        producto_id = str(producto.id_producto)
        if producto_id in self.carrito:
            self.carrito[producto_id]["cantidad"] -= 1
            self.carrito[producto_id]["total"] -= producto.precio
            if self.carrito[producto_id]["cantidad"] < 1:
                self.eliminar(producto)
            else:
                self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
    
    def obtener_subtotal_iva(self):
        subtotal = 0
        for item in self.carrito.values():
            subtotal += item["total"]
        return subtotal * 0.19
    
    def obtener_subtotal(self):
        subtotal = 0
        for item in self.carrito.values():
            subtotal += item["total"]
        return subtotal

    def obtener_total(self):
        total = self.obtener_subtotal()
        # Aquí podrías implementar lógica adicional para descuentos, impuestos, etc., si es necesario
        return total  + self.obtener_subtotal_iva()

 