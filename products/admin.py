# products/admin.py
from django.contrib import admin
from .models import Category, Product

# Registrar Category con opciones básicas
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Columnas que se muestran en la lista
    search_fields = ('name',)      # Campo de búsqueda

# Registrar Product con más opciones
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'is_active')
    list_filter = ('category', 'is_active')  # Filtros laterales
    search_fields = ('name', 'description')  # Búsqueda rápida
    list_editable = ('is_active',)          # Permite cambiar este campo desde la lista
