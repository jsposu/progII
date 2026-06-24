class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def crear_anonimo(cls):
        # 'cls' es equivalente a usar 'Usuario'
        return cls("Anónimo", 0)

    @classmethod
    def desde_cadena(cls, datos: str):
        """Constructor alternativo: recibe 'nombre,edad'"""
        nombre, edad = datos.split(",")
        return cls(nombre.strip(), int(edad.strip()))

    def mostrar(self):
        print(f"Usuario: {self.nombre}, Edad: {self.edad}")

# Uso del constructor normal
u1 = Usuario("María", 25)
u1.mostrar()                           # Usuario: María, Edad: 25

# Uso del constructor alternativo (anónimo)
invitado = Usuario.crear_anonimo()
invitado.mostrar()                     # Usuario: Anónimo, Edad: 0

# Uso del constructor alternativo (desde cadena)
u2 = Usuario.desde_cadena("Pedro, 30")
u2.mostrar()                           # Usuario: Pedro, Edad: 30