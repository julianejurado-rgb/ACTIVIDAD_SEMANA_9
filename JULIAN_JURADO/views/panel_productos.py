import tkinter as tk
from tkinter import ttk
from controllers.gestion_productos import *

def ventana_productos():
    ventana_producto = tk.Toplevel()
    ventana_producto.title("Productos")

    campo_nombre = tk.Entry(ventana_producto)
    campo_precio = tk.Entry(ventana_producto)
    campo_stock = tk.Entry(ventana_producto)
    campo_categoria = tk.Entry(ventana_producto)

    tk.Label(ventana_producto, text="Nombre").grid(row=0, column=0)
    campo_nombre.grid(row=0, column=1)

    tk.Label(ventana_producto, text="Precio").grid(row=1, column=0)
    campo_precio.grid(row=1, column=1)

    tk.Label(ventana_producto, text="Stock").grid(row=2, column=0)
    campo_stock.grid(row=2, column=1)

    tk.Label(ventana_producto, text="Categoria").grid(row=3, column=0)
    campo_categoria.grid(row=3, column=1)

    tabla_productos = ttk.Treeview(
        ventana_producto,
        columns=("ID","Nombre","Precio","Stock","Categoria"),
        show="headings"
    )

    for encabezado in ("ID","Nombre","Precio","Stock","Categoria"):
        tabla_productos.heading(encabezado, text=encabezado)

    tabla_productos.grid(row=6, column=0, columnspan=2)

    def refrescar_datos():
        for elemento in tabla_productos.get_children():
            tabla_productos.delete(elemento)

        for producto in listar_productos():
            tabla_productos.insert("", tk.END, values=producto)

    def guardar_producto():
        registrar_producto(
            campo_nombre.get(),
            float(campo_precio.get()),
            int(campo_stock.get()),
            campo_categoria.get()
        )

        refrescar_datos()

    def eliminar_producto_tabla():
        item = tabla_productos.selection()

        if item:
            producto_id = tabla_productos.item(item)["values"][0]
            borrar_producto(producto_id)
            refrescar_datos()

    tk.Button(ventana_producto, text="Guardar", command=guardar_producto).grid(row=4, column=0)
    tk.Button(ventana_producto, text="Eliminar", command=eliminar_producto_tabla).grid(row=4, column=1)
    tk.Button(ventana_producto, text="Cargar", command=refrescar_datos).grid(row=5, column=0)

    refrescar_datos()
