from django.contrib import admin

from .models import Categoria
from .models import TipoGasto
from .models import Proveedor
from .models import Gasto


admin.site.register(Categoria)
admin.site.register(TipoGasto)
admin.site.register(Proveedor)
admin.site.register(Gasto)