from modelos.visitante import Visitante
from typing import List, Optional

class VisitaServicio:
    def __init__(self):
        self._visitantes: List[Visitante] = []

    def registrar_visitante(self, visitante: Visitante) -> None:
        if self._obtener_por_cedula(visitante.cedula):
            raise ValueError(f"Ya existe un visitante con la cédula {visitante.cedula}.")
        self._visitantes.append(visitante)

    def obtener_todos(self) -> List[Visitante]:
        return self._visitantes

    def actualizar_visitante(self, visitante_actualizado: Visitante) -> None:
        for i, v in enumerate(self._visitantes):
            if v.cedula == visitante_actualizado.cedula:
                self._visitantes[i] = visitante_actualizado
                return
        raise ValueError("No se encontró el visitante.")

    def eliminar_visitante(self, cedula: str) -> None:
        visitante = self._obtener_por_cedula(cedula)
        if visitante:
            self._visitantes.remove(visitante)
        else:
            raise ValueError("El visitante no existe.")

    def _obtener_por_cedula(self, cedula: str) -> Optional[Visitante]:
        for v in self._visitantes:
            if v.cedula == cedula:
                return v
        return None