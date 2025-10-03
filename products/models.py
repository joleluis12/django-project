from django.db import models

# Modelo de Categorías
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


# Modelo de Productos
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='get_products',
    verbose_name='Categoria',
    default=1  # ID de la categoría por defecto
    )
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name
