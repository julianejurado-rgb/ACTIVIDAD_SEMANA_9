import mysql.connector

def conectar():
    conexion_mysql = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tienda"
    )

    return conexion_mysql
