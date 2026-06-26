from flask import render_template
from sqlalchemy import func
from .extensions import db
from .models import Categoria, Producto, Cliente, Pedido

def grafica_productos_categoria():
    datos = (
        db.session.query(
            Categoria.nombre,
            func.count(Producto.id)
        )
        .join(Producto)
        .group_by(Categoria.nombre)
        .all()
    )
    
    etiquetas = [x[0] for x in datos]
    valores = [x[1] for x in datos]

    return render_template(
        "grafica_categoria.html",
        etiquetas=etiquetas,
        valores=valores
        
    )
def grafica_clientes():
    total_clientes = db.session.query(Cliente).count()

    return render_template(
        "grafica_clientes.html",
        total=total_clientes
    )
def grafica_pedidos_cliente():
    datos = (
        db.session.query(
            Cliente.nombre,
            func.count(Pedido.id)
        )
        .join(Pedido)
        .group_by(Cliente.nombre)
        .all()
    )

    etiquetas = [x[0] for x in datos]
    valores = [x[1] for x in datos]

    return render_template(
        "grafica_pedidos.html",
        etiquetas=etiquetas,
        valores=valores
    )