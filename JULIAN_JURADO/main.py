import tkinter as tk

from views.panel_productos import ventana_productos
from views.panel_clientes import ventana_clientes
from utils.informes import *

def abrir_reportes():
    ventana_reportes = tk.Toplevel()
    ventana_reportes.title("Reportes")

    tk.Label(
        ventana_reportes,
        text=f"Total Inventario: {valor_total_inventario()}"
    ).pack()

    tk.Label(
        ventana_reportes,
        text=f"Stock Bajo: {productos_stock_bajo()}"
    ).pack()

ventana_principal = tk.Tk()
ventana_principal.title("Sistema Tienda - Julian")

tk.Button(
    ventana_principal,
    text="Productos",
    command=ventana_productos
).pack()

tk.Button(
    ventana_principal,
    text="Clientes",
    command=ventana_clientes
).pack()

tk.Button(
    ventana_principal,
    text="Reportes",
    command=abrir_reportes
).pack()

ventana_principal.mainloop()
