from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"tipoGastos", views.TipoGastoViewSet)
router.register(r"proveedores", views.ProveedorViewSet)
router.register(r"gastos", views.GastoViewSet)

urlpatterns = [
  path('gastos/sumatoria/', views.total_gastos),
  path('', include(router.urls))
]