from django.urls import path
from . import views

urlpatterns = [
    # Proveedores
    path("proveedores/", views.listar_proveedores, name="listar_proveedores"),
    path("proveedores/<int:pk>/", views.detalle_proveedor, name="detalle_proveedor"),
    path("proveedores/<int:pk>/eliminar/", views.eliminar_proveedor, name="eliminar_proveedor"),

    # Productos
    path("productos/", views.listar_productos, name="listar_productos"),
    path("productos/<int:pk>/", views.detalle_producto, name="detalle_producto"),
    path("productos/<int:pk>/eliminar/", views.eliminar_producto, name="eliminar_producto"),

    # Movimientos
    path("productos/<int:producto_id>/historial/", views.historial_movimientos, name="historial_movimientos"),
]
