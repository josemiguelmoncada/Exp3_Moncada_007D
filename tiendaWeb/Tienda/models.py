import datetime
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User


class Tipo_producto(models.Model):
    id_tipo = models.AutoField(primary_key=True, verbose_name="Id Tipo")
    nombre = models.CharField(max_length=30, verbose_name="Nombre Tipo")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name="Id Producto")
    nombre = models.CharField(max_length=50, verbose_name="Nombre Producto")
    descripcion = models.TextField(verbose_name="Descripción", default="Descripción por defecto")
    ingredientes = models.TextField(verbose_name="Ingredientes", default="Ingredientes por defecto")
    tipo = models.ForeignKey(Tipo_producto, verbose_name="Tipo", on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name="Precio", default=0)
    imagen = models.ImageField(upload_to="img", null=True, verbose_name="Imagen")
    stock = models.IntegerField(verbose_name="Stock", default=0)

    def __str__(self):
        return self.nombre
    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

class DetalleBoleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()
    
    def __str__(self):
        return str(self.id_detalle_boleta)