from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .models import (
    Categoria,
    Proveedor,
    Producto,
    Cliente,
    Pedido,
    DetallePedido,
)


class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)

    list_columns = ["nombre", "descripcion"]
    add_columns = ["nombre", "descripcion"]
    edit_columns = ["nombre", "descripcion"]
    show_columns = ["nombre", "descripcion"]


class ProveedorView(ModelView):
    datamodel = SQLAInterface(Proveedor)

    list_columns = ["nombre", "telefono", "email"]
    add_columns = ["nombre", "telefono", "email"]
    edit_columns = ["nombre", "telefono", "email"]
    show_columns = ["nombre", "telefono", "email"]


class ProductoView(ModelView):
    datamodel = SQLAInterface(Producto)

    list_columns = [
        "nombre",
        "precio",
        "stock",
        "categoria",
        "proveedor",
    ]

    add_columns = [
        "nombre",
        "precio",
        "stock",
        "categoria",
        "proveedor",
    ]

    edit_columns = [
        "nombre",
        "precio",
        "stock",
        "categoria",
        "proveedor",
    ]

    show_columns = [
        "nombre",
        "precio",
        "stock",
        "categoria",
        "proveedor",
    ]


class ClienteView(ModelView):
    datamodel = SQLAInterface(Cliente)

    list_columns = ["nombre", "email", "telefono"]
    add_columns = ["nombre", "email", "telefono"]
    edit_columns = ["nombre", "email", "telefono"]
    show_columns = ["nombre", "email", "telefono"]


class PedidoView(ModelView):
    datamodel = SQLAInterface(Pedido)

    list_columns = ["fecha", "cliente", "total"]
    add_columns = ["fecha", "cliente", "total"]
    edit_columns = ["fecha", "cliente", "total"]
    show_columns = ["fecha", "cliente", "total"]

class DetallePedidoView(ModelView):
    datamodel = SQLAInterface(DetallePedido)

    list_columns = [
        "pedido",
        "producto",
        "cantidad",
        "subtotal",
    ]

    add_columns = [
        "pedido",
        "producto",
        "cantidad",
    ]

    edit_columns = [
        "pedido",
        "producto",
        "cantidad",
    ]

    show_columns = [
        "pedido",
        "producto",
        "cantidad",
        "subtotal",
    ]

    def pre_add(self, item):
        item.subtotal = item.cantidad * item.producto.precio

    def pre_update(self, item):
        item.subtotal = item.cantidad * item.producto.precio