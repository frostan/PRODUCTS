from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductsViewSet

router = DefaultRouter()
router.register('products', ProductsViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]
