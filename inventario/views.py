from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Proveedor, Movimiento, Categoria, Bodega
from django.http import HttpResponse

# ------- CRUD Proveedor -------
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "inventario/listar_proveedores.html", {"proveedores": proveedores})

def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, "inventario/detalle_proveedor.html", {"proveedor": proveedor})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect("listar_proveedores")


# ------- CRUD Producto -------
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "inventario/listar_productos.html", {"productos": productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "inventario/detalle_producto.html", {"producto": producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect("listar_productos")


# ------- Movimientos -------
def historial_movimientos(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    movimientos = Movimiento.objects.filter(producto=producto).order_by("-fecha")
    return render(request, "inventario/historial.html", {"producto": producto, "movimientos": movimientos})

