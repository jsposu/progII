from typing import final

class Padre:

    @final
    def metodo_sagrado(self):
        print("No me cambies.")

    def metodo_normal(self):
        print("Este sí puedes sobreescribir.")

class Hijo(Padre):
    # Un linter (como MyPy) marcará esto como ERROR:
    # def metodo_sagrado(self):
    #     print("Intentando cambiarlo.")

    def metodo_normal(self):
        print("Hijo sobreescribe el método normal correctamente.")

# Uso
padre = Padre()
padre.metodo_sagrado()   # No me cambies.
padre.metodo_normal()    # Este sí puedes sobreescribir.

hijo = Hijo()
hijo.metodo_sagrado()    # No me cambies. (heredado, no sobreescrito)
hijo.metodo_normal()     # Hijo sobreescribe el método normal correctamente.