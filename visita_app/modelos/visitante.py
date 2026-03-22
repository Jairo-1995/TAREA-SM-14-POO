class Visitante:
    def __init__(self, cedula: str, nombre: str, motivo: str):
        self.cedula = cedula
        self.nombre = nombre
        self.motivo = motivo
    
    @property
    def cedula(self) -> str:
        return self._cedula

    @cedula.setter
    def cedula(self, value: str):
        if not value or not value.strip():
            raise ValueError("La cédula no puede estar vacía.")
        
        value = value.strip()

        if not value.isdigit() or len(value) != 10:
            raise ValueError("Ingrese una cédula de 10 dígitos.")

        self._cedula = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        if not value or not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value.strip()

    @property
    def motivo(self) -> str:
        return self._motivo

    @motivo.setter
    def motivo(self, value: str):
        self._motivo = value.strip()