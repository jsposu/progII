class Conversor:
    FACTOR = 1609.344

    def __init__(self, millas):
        if millas < 0:
            raise ValueError("El valor no puede ser negativo")
        self.millas = millas

    def convertir(self):
        return self.millas * self.FACTOR


class ConversorDetallado(Conversor):
    def __init__(self, millas):
        super().__init__(millas)

    def convertir(self):  # sobreescritura
        metros = super().convertir()
        print(f"{self.millas} millas = {metros:.2f} metros")
        return metros

c = ConversorDetallado(5)
c.convertir()
# resultado : 5 millas = 8046.72 metros