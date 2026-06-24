from typing import final

@final
class Base:
    """Esta clase NO debe ser heredada."""
    def saludar(self):
        print("Hola desde Base.")

# Un linter (como MyPy) marcará esto como ERROR:
# class Derivada(Base):
#     pass

# Uso correcto: instanciar directamente
obj = Base()
obj.saludar()  # Hola desde Base.

print("Nota: Python ejecutará el código aunque heredes de @final,")
print("pero MyPy o el linter de VS Code lo marcará como error.")