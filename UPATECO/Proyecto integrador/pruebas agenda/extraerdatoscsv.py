import tkinter as tk

class TablaHorarios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tabla de horarios")

        # Crear un Frame para contener la tabla
        self.tabla_frame = tk.Frame(self)
        self.tabla_frame.pack()

        # Encabezados de columna con los días de la semana
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        for i, dia in enumerate(dias_semana):
            dia_label = tk.Label(self.tabla_frame, text=dia)
            dia_label.grid(row=0, column=i+1)

        # Filas con las horas del día
        hora_inicio = 8
        hora_final = 20
        for hora in range(hora_inicio, hora_final + 1):
            hora_label = tk.Label(self.tabla_frame, text=f"{hora}:00")
            hora_label.grid(row=hora-hora_inicio+1, column=0)

        # Matriz de widgets Label para la tabla
        self.labels = []
        for i in range(hora_inicio, hora_final+1):
            row = []
            for j in range(len(dias_semana)):
                label = tk.Label(self.tabla_frame, text="")
                label.grid(row=i-hora_inicio+1, column=j+1)
                row.append(label)
            self.labels.append(row)

        # Agregar algunos eventos a la tabla
        eventos = [
            {"hora": 10, "dia": "Lunes", "texto": "Reunión"},
            {"hora": 14, "dia": "Miércoles", "texto": "Cita médica"},
            {"hora": 18, "dia": "Viernes", "texto": "Ir al gimnasio"}
        ]
        for evento in eventos:
            hora = evento["hora"]
            dia = evento["dia"]
            texto = evento["texto"]
            fila = hora - hora_inicio
            columna = dias_semana.index(dia)
            label = self.labels[fila][columna]
            label.config(text=texto, bg="yellow", padx=5, pady=5)

tabla_horarios = TablaHorarios()
tabla_horarios.mainloop()

