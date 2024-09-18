from rest_framework import mixins, viewsets
from product.models import Products
from api.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    http_method_names = ['get', 'post', 'delete']
