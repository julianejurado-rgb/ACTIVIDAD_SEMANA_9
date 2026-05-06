import tkinter as tk
from tkinter import ttk
from controllers.gestion_clientes import *

def ventana_clientes():
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("Clientes")

    entrada_nombre = tk.Entry(ventana_cliente)
    entrada_apellido = tk.Entry(ventana_cliente)
    entrada_email = tk.Entry(ventana_cliente)
    entrada_historial = tk.Entry(ventana_cliente)

    tk.Label(ventana_cliente, text="Nombre").grid(row=0, column=0)
    entrada_nombre.grid(row=0, column=1)

    tk.Label(ventana_cliente, text="Apellidos").grid(row=1, column=0)
    entrada_apellido.grid(row=1, column=1)

    tk.Label(ventana_cliente, text="Email").grid(row=2, column=0)
    entrada_email.grid(row=2, column=1)

    tk.Label(ventana_cliente, text="Historial").grid(row=3, column=0)
    entrada_historial.grid(row=3, column=1)

    tabla_clientes = ttk.Treeview(
        ventana_cliente,
        columns=("ID","Nombre","Apellidos","Email","Historial"),
        show="headings"
    )

    for columna in ("ID","Nombre","Apellidos","Email","Historial"):
        tabla_clientes.heading(columna, text=columna)

    tabla_clientes.grid(row=6, column=0, columnspan=2)

    def actualizar_tabla():
        for elemento in tabla_clientes.get_children():
            tabla_clientes.delete(elemento)

        for cliente in listar_clientes():
            tabla_clientes.insert("", tk.END, values=cliente)

    def guardar_cliente():
        registrar_cliente(
            entrada_nombre.get(),
            entrada_apellido.get(),
            entrada_email.get(),
            float(entrada_historial.get())
        )

        actualizar_tabla()

    def eliminar_cliente_tabla():
        item = tabla_clientes.selection()

        if item:
            cliente_id = tabla_clientes.item(item)["values"][0]
            borrar_cliente(cliente_id)
            actualizar_tabla()

    tk.Button(ventana_cliente, text="Guardar", command=guardar_cliente).grid(row=4, column=0)
    tk.Button(ventana_cliente, text="Eliminar", command=eliminar_cliente_tabla).grid(row=4, column=1)
    tk.Button(ventana_cliente, text="Cargar", command=actualizar_tabla).grid(row=5, column=0)

    actualizar_tabla()
