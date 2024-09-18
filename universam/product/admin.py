from django.contrib import admin

from product.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
