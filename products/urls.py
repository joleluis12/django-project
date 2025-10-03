from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

# Crear el router de DRF
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

# Incluir las rutas del router en urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
