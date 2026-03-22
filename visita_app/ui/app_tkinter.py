#==================
#ui tkinter
#==================
import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class AppVisitas(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio

        self.title("Sistema de Registro de Visitantes")
        self.geometry("800x500")
        self.configure(bg="#40596B")

        self._aplicar_estilos()
        self._configurar_interfaz()
        self._actualizar_tabla()

    # ================= ESTILOS =================
    def _aplicar_estilos(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Treeview",
                        background="#aabbd3",
                        foreground="black",
                        rowheight=28,
                        fieldbackground="#aabad1")

        style.map("Treeview",
                  background=[("selected", "#00a8ff")])

        style.configure("Treeview.Heading",
                        background="#75B8AE",
                        foreground="white",
                        font=("Arial", 10, "bold"))

        style.configure("Success.TButton", background="#4cd137", foreground="black", padding=6)
        style.configure("Primary.TButton", background="#00a8ff", foreground="black", padding=6)
        style.configure("Danger.TButton", background="#e84118", foreground="black", padding=6)
        style.configure("Warning.TButton", background="#fbc531", foreground="black", padding=6)

    # ================= UI =================
    def _configurar_interfaz(self):
        # TÍTULO
        tk.Label(self, text="REGISTRO DE VISITANTES",
                 bg="#C1C1EB", fg="#0e0f0f",
                 font=("Arial", 18, "bold")).pack(pady=10)

        # FORMULARIO
        form = tk.Frame( self, bg="#40596B" )
        form.pack(pady=10)
        tk.Label(form, text="Cédula", bg="#B0D2EB", fg="black").grid(row=0, column=0)
        self.ent_cedula = ttk.Entry(form, width=20)
        self.ent_cedula.grid(row=0, column=1, padx=10)

        tk.Label(form, text="Nombre", bg="#B0D2EB", fg="black").grid(row=0, column=2)
        self.ent_nombre = ttk.Entry(form, width=30)
        self.ent_nombre.grid(row=0, column=3, padx=10)

        tk.Label(form, text="Motivo", bg="#B0D2EB", fg="black").grid(row=1, column=0)
        self.ent_motivo = ttk.Entry(form, width=60)
        self.ent_motivo.grid(row=1, column=1, columnspan=3, pady=5)

        # BOTONES
        botones = tk.Frame(self, bg="#40596B")
        botones.pack(pady=10)

        ttk.Button(botones, text="Registrar", style="Success.TButton", command=self._registrar).grid(row=0, column=0, padx=5)
        ttk.Button(botones, text="Actualizar", style="Primary.TButton", command=self._actualizar).grid(row=0, column=1, padx=5)
        ttk.Button(botones, text="Eliminar", style="Danger.TButton", command=self._eliminar).grid(row=0, column=2, padx=5)
        ttk.Button(botones, text="Limpiar", style="Warning.TButton", command=self._limpiar_campos).grid(row=0, column=3, padx=5)

        # TABLA
        self.tabla = ttk.Treeview(self, columns=("cedula", "nombre", "motivo"), show="headings")
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("motivo", text="Motivo")
        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_fila)

    # ================= FUNCIONES =================

    def _registrar(self):
        try:
            visitante = Visitante(
                self.ent_cedula.get().strip(),  # 🔹 SIEMPRE string
                self.ent_nombre.get(),
                self.ent_motivo.get()
            )

            self.servicio.registrar_visitante(visitante)

            self._actualizar_tabla()
            self._limpiar_campos()

            messagebox.showinfo("Éxito", "Visitante registrado correctamente")

        except Exception as e:
            messagebox.showwarning("Error", str(e))
            
    def _actualizar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un visitante para actualizar")
            return

        item = self.tabla.item(seleccion[0])
        cedula = str(item["values"][0])  # 🔹 SIEMPRE string (NO int)

        try:
            visitante = Visitante(
                cedula,
                self.ent_nombre.get(),
                self.ent_motivo.get()
            )

            self.servicio.actualizar_visitante(visitante)

            self._actualizar_tabla()
            self._limpiar_campos()

            messagebox.showinfo("Éxito", "Actualizado correctamente")

        except Exception as e:
            messagebox.showwarning("Error", str(e))

    def _eliminar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un visitante para eliminar")
            return

        item = self.tabla.item(seleccion[0])
        cedula = str(item["values"][0])  # 🔹 SIEMPRE string

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que quieres eliminar la cédula {cedula}?"
        )

        if confirmar:
            try:
                self.servicio.eliminar_visitante(cedula)

                self._actualizar_tabla()
                self._limpiar_campos()

            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for v in self.servicio.obtener_todos():
            self.tabla.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    def _seleccionar_fila(self, event):
        seleccion = self.tabla.selection()

        if seleccion:
            item = self.tabla.item(seleccion[0])
            valores = item["values"]

            self._limpiar_campos()

            # guardamos la cedula original
            self.cedula_original = str(valores[0])

            self.ent_cedula.insert(0, valores[0])
            self.ent_nombre.insert(0, valores[1])
            self.ent_motivo.insert(0, valores[2])


    def _limpiar_campos(self):
        self.cedula_original = None

        self.ent_cedula.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_motivo.delete(0, tk.END)