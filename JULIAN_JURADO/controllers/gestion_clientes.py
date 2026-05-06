from database.base_datos import conectar

def registrar_cliente(nombre_cliente, apellido_cliente, correo_cliente, compras_historial):
    conexion_db = conectar()
    puntero = conexion_db.cursor()

    puntero.execute(
        "INSERT INTO clientes (nombre, apellidos, email, historial_compras) VALUES (%s,%s,%s,%s)",
        (nombre_cliente, apellido_cliente, correo_cliente, compras_historial)
    )

    conexion_db.commit()
    conexion_db.close()

def listar_clientes():
    conexion_db = conectar()
    puntero = conexion_db.cursor()

    puntero.execute("SELECT * FROM clientes")
    registros = puntero.fetchall()

    conexion_db.close()
    return registros

def borrar_cliente(cliente_id):
    conexion_db = conectar()
    puntero = conexion_db.cursor()

    puntero.execute("DELETE FROM clientes WHERE id=%s", (cliente_id,))

    conexion_db.commit()
    conexion_db.close()
