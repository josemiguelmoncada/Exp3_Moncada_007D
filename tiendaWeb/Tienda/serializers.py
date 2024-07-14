from rest_framework import serializers
from .models import Producto

#crear la serializacion de Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        