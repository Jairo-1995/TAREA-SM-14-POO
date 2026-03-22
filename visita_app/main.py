from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas

if __name__ == "__main__":
    servicio = VisitaServicio()
    app = AppVisitas(servicio)
    app.mainloop()