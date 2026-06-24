class Persona:
    # Atributo estático (compartido por todas las instancias)
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1  # Se accede con el nombre de la clase

    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")

# Uso
p1 = Persona("Ana")
p2 = Persona("Luis")
p3 = Persona("Carlos")

p1.presentarse()
p2.presentarse()
p3.presentarse()

# El contador es compartido por todas las instancias
print(f"Total de personas creadas: {Persona.contador}")  # 3