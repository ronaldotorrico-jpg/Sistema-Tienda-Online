from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

from .models import Producto, Cliente, Pedido
from .extensions import db

def reporte_productos():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setTitle("Reporte de Productos")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(180, 750, "REPORTE DE PRODUCTOS")

    y = 720
    pdf.setFont("Helvetica", 10)

    productos = db.session.query(Producto).all()

    for p in productos:
        pdf.drawString(
            40,
            y,
            f"{p.nombre} | Precio: {p.precio} | Stock: {p.stock}"
        )
        y -= 20

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 750

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="reporte_productos.pdf",
        mimetype="application/pdf",
    )


def reporte_clientes():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setTitle("Reporte de Clientes")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(190, 750, "REPORTE DE CLIENTES")

    y = 720
    pdf.setFont("Helvetica", 10)

    clientes = db.session.query(Cliente).all()

    for c in clientes:
        pdf.drawString(
            40,
            y,
            f"{c.nombre} | {c.email} | {c.telefono}"
        )
        y -= 20

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 750

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="reporte_clientes.pdf",
        mimetype="application/pdf",
    )


def reporte_pedidos():
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setTitle("Reporte de Pedidos")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(195, 750, "REPORTE DE PEDIDOS")

    y = 720
    pdf.setFont("Helvetica", 10)

    pedidos = db.session.query(Pedido).all()

    for p in pedidos:
        pdf.drawString(
            40,
            y,
            f"Fecha: {p.fecha} | Cliente: {p.cliente} | Total: {p.total}"
        )
        y -= 20

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 750

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="reporte_pedidos.pdf",
        mimetype="application/pdf",
    )