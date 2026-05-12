text = input(str("Ingresa un string: "))
#contar palabras
contar = len(text.split())
print("Existen", contar, "palabras")
#palabra mas larga
larga = max(text.split(), key=len)
print("La palabra mas larga es:", larga)
#frecuencia de letras en porcentaje XD?
text.lower()
total = len(text)
print("Frecuencias:")
for char in sorted(set(text)):
    if char == " ":
        continue
    else:
        cantidad = text.count(char)
        porcentaje = (cantidad / total) * 100
        print(f"'{char}': {cantidad} veces ({porcentaje:.0f}%)") # un print demencia, se usa el f para poner el % luego de imprimir porcentaje 0_0