import tkinter as tk
import datetime
from tkcalendar import Calendar
class GrillaSemana(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Grilla Semanal")
        self.fecha_inicio = datetime.date(2023, 3, 11) # Año, mes, día
        self.hora_inicio = datetime.time(0, 0) # Hora, minuto
        self.actualizar_grilla()

    # Funciones para avanzar y retroceder fecha en una semana
    def avanzar_semana(self):
        self.fecha_inicio += datetime.timedelta(weeks=1)
        self.actualizar_grilla()

    def retroceder_semana(self):
        self.fecha_inicio -= datetime.timedelta(weeks=1)
        self.actualizar_grilla()

    # Función para actualizar la grilla con la fecha actual
    def actualizar_grilla(self):
        # Limpiar grilla actual
        for widget in self.winfo_children():
            widget.destroy()

        # Actualizar etiqueta de la fecha
        fecha_str = self.fecha_inicio.strftime("%d/%m/%Y")
        fecha_label = tk.Label(self, text=fecha_str)
        fecha_label.grid(row=0, column=1)

        # Actualizar celdas de la grilla
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for i, dia in enumerate(dias_semana):
            dia_label = tk.Label(self, text=dia)
            dia_label.grid(row=1, column=i+2)

        intervalo = datetime.timedelta(hours=1)
        for i in range(8):
            hora = (datetime.datetime.combine(datetime.date.today(), self.hora_inicio) + i * intervalo).time()
            hora_str = hora.strftime("%H:%M")
            hora_label = tk.Label(self, text=hora_str)
            hora_label.grid(row=i+2, column=1)
            for j in range(7):
                dia = self.fecha_inicio + datetime.timedelta(days=j)
                celda_label = tk.Label(self, text="")
                celda_label.grid(row=i+2, column=j+2)

        # Crear botones para avanzar y retroceder una semana
        avanzar_button = tk.Button(self, text="Avanzar semana", command=self.avanzar_semana)
        avanzar_button.grid(row=0, column=10)

        retroceder_button = tk.Button(self, text="Retroceder semana", command=self.retroceder_semana)
        retroceder_button.grid(row=0, column=0)

if __name__ == "__main__":
    # Crear ventana y frame
    ventana = tk.Tk()

    cal = Calendar(ventana, tooltipdelay=10 ,selectmode = 'day',
               year = 2023, month = 2,
               day = 22, locale='es_AR',date_pattern="dd-mm-yyyy")
    frame = GrillaSemana(master=ventana)
    frame.grid(row=5, column=5)
    cal.grid(row=5, column=0)

    # Iniciar loop de la aplicación
    frame.mainloop()
