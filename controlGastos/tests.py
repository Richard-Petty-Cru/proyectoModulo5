from django.test import TestCase

from .models import Categoria
from .models import TipoGasto
from .models import Proveedor
## 
class TestCategoria(TestCase):
    def test_grabacion_categoria(self):
        q = Categoria(nombre="Alimentación")
        q.save()
        self.assertEqual(Categoria.objects.count(), 1)

class TestTipoGasto(TestCase):
    def test_grabacion_tipo_gasto(self):
        q = TipoGasto(nombre_tipo_gasto="Chamarras")
        q.save()
        self.assertEqual(TipoGasto.objects.count(), 1)


class TestProveedor(TestCase):
    def test_grabacion_proveedor(self):
        q = Proveedor(nombre_proveedor="Feria 16 de julio")
        q.save()
        self.assertEqual(Proveedor.objects.count(), 1)
