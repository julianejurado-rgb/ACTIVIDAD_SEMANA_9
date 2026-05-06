class UsuarioCliente:
    def __init__(self, codigo, nombres, apellidos, correo, historial):
        self.id = codigo
        self.nombre = nombres
        self.apellidos = apellidos
        self.email = correo
        self.historial_compras = historial
