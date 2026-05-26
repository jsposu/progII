from abc import ABC, abstractmethod

class Encriptador(ABC):  # Actúa como interfaz pura

    @abstractmethod
    def encriptar(self, datos: str) -> str:
        pass

    @abstractmethod
    def desencriptar(self, datos: str) -> str:
        pass

class EncriptadorAES(Encriptador):
    def encriptar(self, datos: str) -> str:
        return f"AES({datos})"

    def desencriptar(self, datos: str) -> str:
        return datos.replace("AES(", "").replace(")", "")

# Uso
enc = EncriptadorAES()
mensaje_encriptado = enc.encriptar("Hola Mundo")
print(f"Encriptado: {mensaje_encriptado}")       # Encriptado: AES(Hola Mundo)

mensaje_original = enc.desencriptar(mensaje_encriptado)
print(f"Desencriptado: {mensaje_original}")      # Desencriptado: Hola Mundo

# Si olvidas implementar un método, Python lanzará un TypeError al instanciar.