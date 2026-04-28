# 1. Literal de bytes (Forma mas comun)
mi_byte = b"\xFF"
# 2. Contructor bytes a partir de un entero
mi_byte_dos = bytes([255])
# verificacion
print(type(mi_byte)) # <class 'bytes'>
print(mi_byte[0]) # 255