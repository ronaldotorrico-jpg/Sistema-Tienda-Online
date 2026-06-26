from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date


class Categoria(Model):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(255))

    def __repr__(self):
        return self.nombre


class Proveedor(Model):
    __tablename__ = "proveedor"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20))
    email = Column(String(100))

    def __repr__(self):
        return self.nombre


class Producto(Model):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    categoria_id = Column(Integer, ForeignKey("categoria.id"))
    proveedor_id = Column(Integer, ForeignKey("proveedor.id"))

    categoria = relationship("Categoria")
    proveedor = relationship("Proveedor")

    def __repr__(self):
        return self.nombre


class Cliente(Model):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100))
    telefono = Column(String(20))

    def __repr__(self):
        return self.nombre


class Pedido(Model):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, default=date.today)
    total = Column(Float, default=0)

    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    cliente = relationship("Cliente")

    def __repr__(self):
        return f"Pedido {self.id}"


class DetallePedido(Model):
    __tablename__ = "detalle_pedido"

    id = Column(Integer, primary_key=True)

    pedido_id = Column(Integer, ForeignKey("pedido.id"))
    producto_id = Column(Integer, ForeignKey("producto.id"))

    cantidad = Column(Integer, nullable=False)
    subtotal = Column(Float)

    pedido = relationship("Pedido")
    producto = relationship("Producto")

    def __repr__(self):
        return f"Detalle {self.id}"