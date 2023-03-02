# importar librerias
from tkinter import *
from tkcalendar import Calendar
import datetime

class Evento:
    def __init__(self, titulo, fecha_hora=None, duracion=1, descripcion="", importancia="normal", fecha_hora_recordatorio=None, etiquetas=[]):
        self.titulo = titulo
        self.fecha_hora = fecha_hora if fecha_hora is not None else datetime.datetime.now()
        self.duracion = duracion
        self.descripcion = descripcion
        self.importancia = importancia
        self.fecha_hora_recordatorio = fecha_hora_recordatorio
        self.etiquetas = etiquetas

        
class Calendario:
    def __init__(self):
        self.eventos = []
    
    def crear_evento(self, evento):
        if not self._existe_evento_misma_fecha_hora(evento.fecha_hora):
            self.eventos.append(evento)
        else:
            print("Ya existe un evento en la misma fecha y hora")
    
    def modificar_evento(self, indice, evento):
        if not self._existe_evento_misma_fecha_hora(evento.fecha_hora, indice):
            self.eventos[indice] = evento
        else:
            print("Ya existe un evento en la misma fecha y hora")
    
    def eliminar_evento(self, indice):
        del self.eventos[indice]
    
    def mostrar_eventos(self):
        for i, evento in enumerate(self.eventos):
            print(f"{i}: {evento.titulo} ({evento.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')})")
    
    def mostrar_recordatorios(self):
        ahora = datetime.datetime.now()
        for evento in self.eventos:
            if evento.fecha_hora_recordatorio is not None and evento.fecha_hora_recordatorio < ahora:
                print(f"Recordatorio: {evento.titulo}")
    
    def _existe_evento_misma_fecha_hora(self, fecha_hora, indice_excluir=None):
        for i, evento in enumerate(self.eventos):
            if i != indice_excluir and evento.fecha_hora == fecha_hora:
                return True
        return False





# crear el objeto tk
Form_principal = Tk()
 
# Establecer el tamaño del Form
Form_principal.geometry("400x400")
 
# Añadir un calendario tooltipdelay es el tiempo que demora en mostrar el tooltip
cal = Calendar(Form_principal, tooltipdelay=10 ,selectmode = 'day',
               year = 2023, month = 2,
               day = 22, locale='es_AR')
date = cal.datetime.today()
cal.calevent_create(date, 'aca va un evento', 'mensaje')
cal.calevent_create(date, 'Recordatorio, averiguar como funciona', 'reminder')
cal.calevent_create(date, 'Recordatorio2 el mismo dia', 'reminder')
cal.calevent_create(date + cal.timedelta(days=-2), 'Recordatorio 2 dias antes', 'reminder')
cal.calevent_create(date + cal.timedelta(days=3), '3 dias despues', 'message')
 
cal.pack(pady = 20)
 
def select_fecha():
    date.config(text = "La fecha seleccionada es : " + cal.get_date())
 
# añadir boton y label

Button(Form_principal, text = "Agendar fecha",
       command = select_fecha).pack(pady = 20)
 
date = Label(Form_principal, text = "")
date.pack(pady = 20)
 
# ejecutar tkinter
Form_principal.mainloop()