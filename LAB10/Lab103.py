with open("archivo_demo.txt", "a") as f:
    f.write("Ahora el archivo tiene mas contenido!")

#abrir y leer el archivo despues de agregarlo:
with open("archivo_demo.txt") as f:
    print(f.read())

with open("archivo_demo.txt", "w") as f:
    f.write("ups! he borrado el contenido!")

with open("archivo_demo.txt") as f:
    print(f.read())