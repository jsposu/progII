from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

class Circulo(Figura):
    def __init__(self, r):
        self.r = r
        
    def calcularArea(self):
        return 3.14159 * (self.r ** 2)

class Rectangulo(Figura):
    def __init__(self, b, a):
        self.b = b
        self.a = a
        
    def calcularArea(self):
        return self.b * self.a

class Triangulo(Figura):
    def __init__(self, b, a):
        self.b = b
        self.a = a
        
    def calcularArea(self):
        return (self.b * self.a) / 2

figuras = [Circulo(5), Rectangulo(4, 6), Triangulo(3, 5)]

for f in figuras:
    print(f"{type(f).__name__}: {f.calcularArea():.2f}")