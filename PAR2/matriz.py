matriz = [
    [4, 1, 7],
    [2, 9, 3],
    [5, 8, 6]
]

suma = 0

for fila in matriz:
    for elemento in fila:
        if elemento % 2 == 0:
            suma += elemento

print(suma)