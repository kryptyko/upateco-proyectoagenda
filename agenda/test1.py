import datetime as dt
from datetime import datetime, timedelta



class Evento:
    def __init__(self, titulo, fecha_hora=datetime.now(), duracion=timedelta(hours=1), descripcion='', importancia='normal', fecha_hora_recordatorio=None, etiquetas=None):
        self.titulo = titulo
        self.fecha_hora = fecha_hora
        self.duracion = duracion
        self.descripcion = descripcion
        self.importancia = importancia
        self.fecha_hora_recordatorio = fecha_hora_recordatorio
        self.etiquetas = etiquetas if etiquetas is not None else []

class Calendario:
    def __init__(self):
        self.eventos = []
    
    def crear_evento(self, titulo, fecha_hora=None, duracion=timedelta(hours=1), descripcion='', importancia='normal', fecha_hora_recordatorio=None, etiquetas=None):
        if fecha_hora is None:
            fecha_hora = datetime.now
            if self._existe_evento_misma_fecha_hora(fecha_hora, fecha_hora + duracion):
            print('Error: El evento se superpone con otro evento existente')
            return
        evento = Evento(titulo, fecha_hora, duracion,descripcion , Importancia_evento_str, datetime.datetime(2023, 2, 23, 9), ["reunión", "equipo"])
        evento = Evento(titulo, fecha_hora, duracion, descripcion, importancia, fecha_hora_recordatorio, etiquetas)
        self.eventos.append(evento)
    
    def modificar_evento(self, evento_modificar, titulo=None, fecha_hora=None, duracion=None, descripcion=None, importancia=None, fecha_hora_recordatorio=None, etiquetas=None):
        fecha_hora_original = evento_modificar.fecha_hora
        duracion_original = evento_modificar.duracion
        if fecha_hora is not None and duracion is not None and self._existe_evento_misma_fecha_hora(fecha_hora, fecha_hora + duracion, evento_modificar):
            print('Error: El evento se superpone con otro evento existente')
            return
        evento_modificar.titulo = titulo if titulo is not None else evento_modificar.titulo
        evento_modificar.fecha_hora = fecha_hora if fecha_hora is not None else evento_modificar.fecha_hora
        evento_modificar.duracion = duracion if duracion is not None else evento_modificar.duracion
        evento_modificar.descripcion = descripcion if descripcion is not None else evento_modificar.descripcion
        evento_modificar.importancia = importancia if importancia is not None else evento_modificar.importancia
        evento_modificar.fecha_hora_recordatorio = fecha_hora_recordatorio if fecha_hora_recordatorio is not None else evento_modificar.fecha_hora_recordatorio
        evento_modificar.etiquetas = etiquetas if etiquetas is not None else evento_modificar.etiquetas
        if self._existe_evento_misma_fecha_hora(fecha_hora_original, fecha_hora_original + duracion_original, evento_modificar):
            print('Error: El evento modificado se superpone con otro evento existente')
           


def main():
    calendar = Calendario()
    while True:
        print("""
        Menú de opciones:
        1. Crear un evento
        2. Modificar un evento
        3. Eliminar un evento
        4. Mostrar recordatorio
        5. Buscar eventos
        6. Mostrar calendario semanal
        7. Mostrar calendario mensual
        8. Salir
        """)
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            fecha_hora_str = input("Por favor, ingrese una fecha y hora en el siguiente formato: DD/MM/AAAA HH:MM:SS ")
            fecha_hora =   dt.datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M:%S")
            descripcion_evento=input("ingrese en nombre del evento: ")
            minuta_evento=input("ingrese una referencia del evento")
            duracion_evento=input("ingrese la duracion del evento en hs")
            Importancia_evento=input("el evento tiene calidad de importante? S/N")
            if Importancia_evento=="S":
                Importancia_evento_str="Importante"
            else:
                Importancia_evento_str="Normal"
            
                    
            evento = Evento(descripcion_evento, fecha_hora, duracion_evento,minuta_evento , Importancia_evento_str, dt.datetime(2023, 2, 23, 9), ["reunión", "equipo"])
            calendar.crear_evento(evento)
        elif opcion == "2":
            calendar.modificar_evento(calendar)
        elif opcion == "3":
            calendar.eliminar_evento(calendar)
        elif opcion == "4":
            calendar.mostrar_eventos()
        elif opcion == "5":
            #buscar_eventos(calendar)
            pass
        elif opcion == "6":
            pass
            #mostrar_calendario_semanal(calendar)
        elif opcion == "7":
            pass
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")


main()











"""""



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

# Ejemplo de uso
calendario = Calendario()

# Crear evento
evento = Evento("Reunión de equipo", datetime.datetime(2023, 2, 23, 10), 2, "Discutir el plan de acción para el próximo trimestre", "importante", datetime.datetime(2023, 2, 23, 9), ["reunión", "equipo"])
calendario.crear_evento(evento)

# Modificar evento
evento.descripcion = "Nueva descripción"
calendario.modificar_evento(0, evento)

# Eliminar evento
calendario.eliminar_evento(0)

# Mostrar eventos y recordatorios
calendario.mostrar_eventos()
calendario.mostrar_recordatorios()
"""