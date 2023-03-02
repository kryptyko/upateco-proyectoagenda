import datetime
import json
#modificado0.1
class Evento_class:
    def __init__(self, titulo, fecha_hora=None, duracion=1, descripcion="", importancia="normal", fecha_hora_recordatorio=None, etiquetas=[]):
        self.titulo = titulo
        self.fecha_hora = fecha_hora if fecha_hora is not None else datetime.datetime.now()
        self.duracion = duracion
        self.descripcion = descripcion
        self.importancia = importancia
        self.fecha_hora_recordatorio = fecha_hora_recordatorio
        self.etiquetas = etiquetas

        
class Calendario_class:
    def __init__(self):
        self.eventos_lst = [] #creo una lista  que almacenara los evemtos con un indice que comienza en 0
    
    """
    def crear_evento(self, evento):
         #crea un evento y controla que no exista un evento en la misma hora
        if not self._existe_evento_misma_fecha_hora(evento.fecha_hora):
            self.eventos_lst.append(evento) #añade por medio de append un evento a la lista
        else:
            print("Ya existe un evento en la misma fecha y hora") # en caso de existir un evento en la misma hora advierte
    """
    def crear_evento(self, evento): #se agrego el control de superposicion de eventos
        """ crea un evento y controla que no exista un evento en la misma hora"""
        fecha_hora_fin = evento.fecha_hora + datetime.timedelta(minutes=evento.duracion)
        if not self._existe_evento_misma_fecha_hora(evento.fecha_hora, fecha_hora_fin):
            self.eventos_lst.append(evento)
        else:
            print("Ya existe un evento en la misma fecha y hora")

    
    #modifica el evento, se agrego la duracion del evento
    """def modificar_evento(self, indice, evento):
    #    modifica un evento en base al indice que va de 0 a la lista eventos
        if not self._existe_evento_misma_fecha_hora(evento.fecha_hora, indice):
            self.eventos_lst[indice] = evento
        else:
            print("Ya existe un evento en la misma fecha y hora")
    """
    def modificar_evento(self, indice, evento):
        """modifica un evento en base al indice que va de 0 a la lista eventos"""
        fecha_hora_fin = evento.fecha_hora + datetime.timedelta(minutes=evento.duracion)
        if not self._existe_evento_misma_fecha_hora(evento.fecha_hora, fecha_hora_fin, indice):
            self.eventos_lst[indice] = evento
        else:
            print("Ya existe un evento en la misma fecha y hora")


    def eliminar_evento(self, indice):
        del self.eventos_lst[indice]
    
    def mostrar_eventos(self):
        for i, evento in enumerate(self.eventos_lst):
            print(f"{i}: {evento.titulo} ({evento.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')})")
    
    def mostrar_recordatorios(self):
        ahora = datetime.datetime.now()
        for evento in self.eventos_lst:
            if evento.fecha_hora_recordatorio is not None and evento.fecha_hora_recordatorio < ahora:
                print(f"Recordatorio: {evento.titulo}")
    
    """def _existe_evento_misma_fecha_hora(self, fecha_hora, indice_excluir=None):
        for i, evento in enumerate(self.eventos_lst):
            if i != indice_excluir and evento.fecha_hora == fecha_hora:
                return True
        return False
    """

    def _existe_evento_misma_fecha_hora(self, fecha_hora_inicio, fecha_hora_fin, indice_excluir=None):
        for i, evento in enumerate(self.eventos_lst):
            if i != indice_excluir: 
                if (fecha_hora_inicio < evento.fecha_hora + datetime.timedelta(minutes=evento.duracion) and fecha_hora_fin > evento.fecha_hora) or \
                    (fecha_hora_inicio < evento.fecha_hora and fecha_hora_fin > evento.fecha_hora - datetime.timedelta(minutes=evento.duracion)):
                    return True
        return False
    
    def guardar_eventos(self, archivo):
        """guarda los eventos en un archivo JSON"""
        with open(archivo, 'w') as f:
            eventos_dict = {'eventos': []}
            for evento in self.eventos_lst:
                evento_dict = {
                    'titulo': evento.titulo,
                    'fecha_hora': evento.fecha_hora.isoformat(),
                    'duracion': evento.duracion,
                    'descripcion': evento.descripcion,
                    'importancia': evento.importancia,
                    'fecha_hora_recordatorio': evento.fecha_hora_recordatorio.isoformat() if evento.fecha_hora_recordatorio is not None else None,
                    'etiquetas': evento.etiquetas
                }
                eventos_dict['eventos'].append(evento_dict)
            json.dump(eventos_dict, f, indent=4)
    def cargar_eventos(self, archivo):
        """carga los eventos desde un archivo JSON"""
        with open(archivo, 'r') as f:
            eventos_dict = json.load(f)
            eventos_lst = []
            for evento_dict in eventos_dict['eventos']:
                titulo = evento_dict['titulo']
                fecha_hora = datetime.datetime.fromisoformat(evento_dict['fecha_hora'])
                duracion = evento_dict['duracion']
                descripcion = evento_dict['descripcion']
                importancia = evento_dict['importancia']
                fecha_hora_recordatorio = datetime.datetime.fromisoformat(evento_dict['fecha_hora_recordatorio']) if evento_dict['fecha_hora_recordatorio'] is not None else None
                etiquetas = evento_dict['etiquetas']
                evento = Evento_class(titulo, fecha_hora, duracion, descripcion, importancia, fecha_hora_recordatorio, etiquetas)
                eventos_lst.append(evento)
            self.eventos_lst = eventos_lst
# Ejemplo de uso
#calendario = Calendario()

# Crear evento
"""evento = Evento("Reunión de equipo", datetime.datetime(2023, 2, 23, 10), 2, "Discutir el plan de acción para el próximo trimestre", "importante", datetime.datetime(2023, 2, 23, 9), ["reunión", "equipo"])
calendario.crear_evento(evento)

# Modificar evento
evento.descripcion = "Nueva descripción"
calendario.modificar_evento(0, evento)

# Eliminar evento
calendario.eliminar_evento(0)

# Mostrar eventos y recordatorios
calendario.mostrar_eventos()
calendario.mostrar_recordatorios()"""


def main():
    calendar = Calendario_class()
    calendar.cargar_eventos("eventos.json")
    while True:
        print("""
        Menú de opciones:
        1. Crear un evento
        2. Modificar un evento
        3. Eliminar un evento
        4. Mostrar eventos
        5. Buscar eventos
        6. Mostrar calendario semanal
        7. Mostrar calendario mensual
        8. Mostrar recordatorios
        9. Salir
        """)
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            fecha_hora_str = input("Por favor, ingrese una fecha y hora en el siguiente formato: DD/MM/AAAA HH:MM:SS ")
            fecha_hora = datetime.datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M:%S")
            descripcion_evento=input("ingrese en nombre del evento: ")
            minuta_evento=input("ingrese una referencia del evento: ")
            duracion_evento=float(input("ingrese la duracion del evento en minutos: "))
            Importancia_evento=input("el evento tiene calidad de importante? S/N")
            if Importancia_evento=="S":
                Importancia_evento_str="Importante"
            else:
                Importancia_evento_str="Normal"
            
                    
            evento_var = Evento_class(descripcion_evento, fecha_hora, duracion_evento,minuta_evento , Importancia_evento_str, datetime.datetime(2023, 2, 23, 9), ["reunión", "equipo"])
            calendar.crear_evento(evento_var)
            calendar.guardar_eventos("eventos.json")
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
        elif opcion == "8":
            calendar.mostrar_recordatorios(calendar)
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")


main()