from django import views
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Categoria
from .models import TipoGasto
from .models import Proveedor
from .models import Gasto

from .serializers import CategoriaSerializer
from .serializers import TipoGastoSerializer
from .serializers import ProveedorSerializer
from .serializers import GastoSerializer



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TipoGastoViewSet(viewsets.ModelViewSet):
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer


#CUSTOM API
@api_view(["GET"])
def total_gastos(request):
    """
    Sumatoria de gastos 
    """
    try:
       
        sumatoria_gastos = Gasto.objects.count()
        return JsonResponse(
            {
                "sumatoria_gastos": sumatoria_gastos
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)