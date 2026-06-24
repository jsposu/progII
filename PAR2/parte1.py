class Matriz:
    def __init__(self, datos):
        self.datos = datos

    def suma_pares(self):
        suma = 0
        for fila in self.datos:
            for elemento in fila:
                if elemento % 2 == 0:
                    suma += elemento
        print(suma)
        return suma

class MatrizEstadistica(Matriz):
    def __init__(self, datos):
        super().__init__(datos)

    def suma_pares(self):
        suma = 0
        pares = []
        for fila in self.datos:
            for elemento in fila:
                if elemento % 2 == 0:
                    suma += elemento
                    pares.append(elemento)
        promedio = suma / len(pares) if pares else 0
        print(f"Suma pares: {suma}")
        print(f"Promedio pares: {promedio}")
        return suma

matriz = [
    [4, 1, 7],
    [2, 9, 3],
    [5, 8, 6]
]

m = MatrizEstadistica(matriz)
m.suma_pares()