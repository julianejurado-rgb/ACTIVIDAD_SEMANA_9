from database.base_datos import conectar

def registrar_producto(nombre_producto, valor_producto, cantidad_stock, tipo_categoria):
    conexion_db = conectar()
    cursor_db = conexion_db.cursor()

    cursor_db.execute(
        "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (%s,%s,%s,%s)",
        (nombre_producto, valor_producto, cantidad_stock, tipo_categoria)
    )

    conexion_db.commit()
    conexion_db.close()

def listar_productos():
    conexion_db = conectar()
    cursor_db = conexion_db.cursor()

    cursor_db.execute("SELECT * FROM productos")
    resultados = cursor_db.fetchall()

    conexion_db.close()
    return resultados

def borrar_producto(codigo_producto):
    conexion_db = conectar()
    cursor_db = conexion_db.cursor()

    cursor_db.execute("DELETE FROM productos WHERE id=%s", (codigo_producto,))

    conexion_db.commit()
    conexion_db.close()
