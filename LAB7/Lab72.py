n = int(input("Ingrese un numero "))
if n % 2 == 0:
    for Y in range(n):
        for X in range(n):
            if Y == X:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
else:
    print("coloca un numero par")