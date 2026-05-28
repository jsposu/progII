class CalculadoraFactorial:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            return "No se puede calcular el factorial de un número negativo."
        
        factorial = 1
        for i in range(1, self.numero + 1):
            factorial *= i
        return factorial

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número (N) para calcular su factorial: "))
        mi_calculadora = CalculadoraFactorial(n)
        resultado = mi_calculadora.calcular()
        print(f"El factorial de {n} es: {resultado}")
        
    except ValueError:
        print("Por favor, introduce un número entero válido.")