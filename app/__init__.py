from flask import Flask
from .extensions import appbuilder, db
from .views import (
    CategoriaView,
    ProveedorView,
    ProductoView,
    ClienteView,
    PedidoView,
    DetallePedidoView,
)
from .reportes import (
    reporte_productos,
    reporte_clientes,
    reporte_pedidos,
)
from .graficas import (
    grafica_productos_categoria,
    grafica_clientes,
    grafica_pedidos_cliente,
)


def create_app():
    app = Flask(__name__)

    # Mostrar la carpeta static en la terminal
    print("Carpeta static:", app.static_folder)

    app.config.from_object("config")

    db.init_app(app)

    with app.app_context():
        appbuilder.init_app(app, db.session)
        db.create_all()

        appbuilder.add_view(
            CategoriaView,
            "Categorias",
            icon="fa-tags",
            category="Tienda Online",
        )

        appbuilder.add_view(
            ProveedorView,
            "Proveedores",
            icon="fa-truck",
            category="Tienda Online",
        )

        appbuilder.add_view(
            ProductoView,
            "Productos",
            icon="fa-shopping-cart",
            category="Tienda Online",
        )

        appbuilder.add_view(
            ClienteView,
            "Clientes",
            icon="fa-users",
            category="Tienda Online",
        )

        appbuilder.add_view(
            PedidoView,
            "Pedidos",
            icon="fa-file",
            category="Tienda Online",
        )

        appbuilder.add_view(
            DetallePedidoView,
            "Detalle Pedido",
            icon="fa-list",
            category="Tienda Online",
        )

    # Reportes
    app.add_url_rule(
        "/reporte/productos",
        "reporte_productos",
        reporte_productos,
    )

    app.add_url_rule(
        "/reporte/clientes",
        "reporte_clientes",
        reporte_clientes,
    )

    app.add_url_rule(
        "/reporte/pedidos",
        "reporte_pedidos",
        reporte_pedidos,
    )

    # Gráficas
    app.add_url_rule(
        "/grafica/categoria",
        "grafica_categoria",
        grafica_productos_categoria,
    )

    app.add_url_rule(
        "/grafica/clientes",
        "grafica_clientes",
        grafica_clientes,
    )

    app.add_url_rule(
        "/grafica/pedidos",
        "grafica_pedidos",
        grafica_pedidos_cliente,
    )

    return app


app = create_app()