from database.base_datos import conectar

def valor_total_inventario():
    conexion_db = conectar()
    cursor_db = conexion_db.cursor()

    cursor_db.execute("SELECT SUM(precio * stock) FROM productos")
    inventario_total = cursor_db.fetchone()[0]

    conexion_db.close()
    return inventario_total

def productos_stock_bajo(limite=5):
    conexion_db = conectar()
    cursor_db = conexion_db.cursor()

    cursor_db.execute("SELECT COUNT(*) FROM productos WHERE stock < %s", (limite,))
    total_productos = cursor_db.fetchone()[0]

    conexion_db.close()
    return total_productos
