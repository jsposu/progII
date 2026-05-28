from abc import ABC, abstractmethod
import math

class FuncionMatematica(ABC):
    @abstractmethod
    def evaluar(self, x):
        pass

class FuncionLineal(FuncionMatematica):
    def __init__(self, m, b):
        self.m = m
        self.b = b
        
    def evaluar(self, x):
        return self.m * x + self.b

class FuncionCuadratica(FuncionMatematica):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def evaluar(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

class FuncionExponencial(FuncionMatematica):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def evaluar(self, x):
        return self.a * math.exp(self.b * x)

funciones = [
    FuncionLineal(2, 3),        # f(x) = 2x + 3
    FuncionCuadratica(1, -2, 1), # f(x) = 1x² - 2x + 1
    FuncionExponencial(2, 0.5)   # f(x) = 2 * e^(0.5x)
]

x_valor = 2

for f in funciones:
    print(f"{type(f).__name__}: f({x_valor}) = {f.evaluar(x_valor):.4f}")