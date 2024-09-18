from rest_framework import serializers
from product.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    """GET POST DELETE Сериализатор"""

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price')
