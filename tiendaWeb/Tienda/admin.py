from django.contrib import admin
from .models import Producto, Tipo_producto, Boleta, DetalleBoleta

# Register your models here.
admin.site.register(Producto)
admin.site.register(Tipo_producto)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)