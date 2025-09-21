from django.contrib import admin
from .models import Categoria, Proveedor, Bodega, Producto, Movimiento

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sku", "categoria", "proveedor", "precio", "stock_actual")
    search_fields = ("nombre", "sku")
    list_filter = ("categoria", "proveedor")

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Bodega)
admin.site.register(Movimiento)

