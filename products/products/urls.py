from django.contrib import admin
from django.urls import path, include
from product.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', index, name='index')
]
