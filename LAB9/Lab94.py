class Calculadora:

    @staticmethod
    def sumar(a, b):
        return a + b  # No usa 'self' ni 'cls'

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            print("Error: no se puede dividir entre cero.")
            return None
        return a / b

# Se llama directamente sin instanciar
resultado = Calculadora.sumar(5, 3)
print(f"5 + 3 = {resultado}")           # 8

print(f"10 - 4 = {Calculadora.restar(10, 4)}")        # 6
print(f"6 * 7 = {Calculadora.multiplicar(6, 7)}")     # 42
print(f"15 / 3 = {Calculadora.dividir(15, 3)}")       # 5.0