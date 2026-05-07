miTupla = ("asignacion", "laboratorio", "python")
myit = iter(miTupla)

print(next(myit))   # asignacion
print(next(myit))   # laboratorio
print(next(myit))   # python

mystr = "casa"
myit = iter(mystr)

print(next(myit))   # c
print(next(myit))   # a
print(next(myit))   # s
print(next(myit))   # a

for x in mystr:
    print(x)
