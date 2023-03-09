import csv
from datetime import datetime, timedelta

class Agenda:
    def __init__(self):
        self.eventos = []  #creo la variable que almacena los eventos
        self.id_counter = 0 #inicializo el contador de id de eventos
        
    def agregar_evento(self, fecha, hora, duracion, importancia, criterios, detalle):
        """ metodo para agergar un evento"""
        fecha_hora = datetime.strptime(fecha + " " + hora, "%d/%m/%Y %H:%M")
        fin_evento = fecha_hora + timedelta(hours=int(duracion.split()[0]))
        if self.verificar_superposicion(fecha_hora, fin_evento):
            print("El nuevo evento se superpone con otro evento existente en la agenda.")
            return

        nuevo_evento = {"id": self.id_counter, "fecha": fecha, "hora": hora, "duracion": duracion, 
                        "importancia": importancia, "criterios": criterios, "detalle": detalle}
        self.eventos.append(nuevo_evento) #agrego el evento
        self.id_counter += 1  #sumo 1 al contador de eventos
    def verificar_superposicion(self, fecha_hora, fin_evento):
        # Verificar si hay algún evento que se superponga con el nuevo evento
        for evento in self.eventos:
            inicio_evento = datetime.strptime(evento["fecha"] + " " + evento["hora"], "%d/%m/%Y %H:%M")
            fin_evento_existente = inicio_evento + timedelta(hours=int(evento["duracion"].split()[0]))
            if inicio_evento <= fecha_hora < fin_evento_existente or inicio_evento < fin_evento <= fin_evento_existente:
                return True
        
        return False



    def mostrar_eventos(self):
        """ metodo para mostrar los eventos"""
        eventos_ordenados = sorted(self.eventos, key=lambda evento: evento["id"]) #ordeno los eventos por numero de id
        for evento in eventos_ordenados: #recorro la lista de eventos evento por evento
            print("ID: ", evento["id"])
            print("Fecha: ", evento["fecha"])
            print("Hora: ", evento["hora"])
            print("Duración: ", evento["duracion"])
            print("Importancia: ", evento["importancia"])
            print("Criterios de búsqueda: ", evento["criterios"])
            print("Detalle: ", evento["detalle"])
            print()
        
    def modificar_evento(self, id, fecha=None, hora=None, duracion=None, importancia=None, criterios=None, detalle=None):
        """metodo para modificar un evento por numero de id, le tengo q pasar como parametro el id y alguno de los atributos a modificar"""
        evento_encontrado = False
        for evento in self.eventos: #recorro los paramtros ingresados en busqueda de algo para modificar, si el valor es none no modifico nada
            if evento["id"] == id: #recorro la lista de eventos por id si la encuentro hago lo que sigue
                if fecha is not None: #si el atributo tiene un valos distinto a none lo modifico
                    evento["fecha"] = fecha
                if hora is not None:
                    evento["hora"] = hora
                if duracion is not None:
                    evento["duracion"] = duracion
                if importancia is not None:
                    evento["importancia"] = importancia
                if criterios is not None:
                    evento["criterios"] = criterios
                if detalle is not None:
                    evento["detalle"] = detalle
                evento_encontrado = True
                break
        if not evento_encontrado:
            print("No se encontró un evento con el ID especificado.")
    
    def eliminar_evento(self, id):
        """metodo para eliminar un evento"""
        evento_encontrado = False
        for evento in self.eventos:
            if evento["id"] == id:
                self.eventos.remove(evento)
                evento_encontrado = True
                break
        if not evento_encontrado:
            print("No se encontró un evento con el ID especificado.")

    def buscar_por_fecha(self, fecha):
        """busco eventos por fecha"""
        eventos_encontrados = []
        for evento in self.eventos:
            if evento["fecha"] == fecha:
                eventos_encontrados.append(evento)
        if eventos_encontrados:
            print("Eventos encontrados:")
            for evento in eventos_encontrados:
                print("ID: ", evento["id"])
                print("Fecha: ", evento["fecha"])
                print("Hora: ", evento["hora"])
                print("Duración: ", evento["duracion"])
                print("Importancia: ", evento["importancia"])
                print("Criterios de búsqueda: ", evento["criterios"])
                print("Detalle: ", evento["detalle"])
                print()
        else:
            print("No se encontraron eventos en la fecha especificada.")
    
    def buscar_por_importancia(self, importancia):
        eventos_encontrados = []
        for evento in self.eventos:
            if evento["importancia"] == importancia:
                eventos_encontrados.append(evento)
        if eventos_encontrados:
            print("Eventos encontrados:")
            for evento in eventos_encontrados:
                print("ID: ", evento["id"])
                print("Fecha: ", evento["fecha"])
                print("Hora: ", evento["hora"])
                print("Duración: ", evento["duracion"])
                print("Importancia: ", evento["importancia"])
                print("Criterios de búsqueda: ", evento["criterios"])
                print("Detalle: ", evento["detalle"])
                print()
        else:
            print("No se encontraron eventos con la importancia especificada.")

    def exportar_a_csv(self, nombre_archivo):
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            campos = ["id", "fecha", "hora", "duracion", "importancia", "criterios", "detalle"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            for evento in self.eventos:
                escritor.writerow(evento)
    
    def importar_desde_csv(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                self.agregar_evento(fila["fecha"], fila["hora"], fila["duracion"], fila["importancia"], fila["criterios"], fila["detalle"])


agenda = Agenda()
agenda.importar_desde_csv("events.csv")
agenda.agregar_evento("12/03/2023", "10:00", "1 hora", "Alta", "Reunión de trabajo", "Presentación del proyecto")
#agenda.agregar_evento("15/03/2023", "14:00", "2 horas", "Media", "Entrevista de trabajo", "Conocer al equipo")
#agenda.agregar_evento("18/03/2023", "16:00", "3 horas", "Baja", "Cita médica", "Chequeo anual")
#agenda.mostrar_eventos()
#agenda.modificar_evento(1, importancia="Alta", detalle="Presentación del proyecto actualizada") #modifico un evento
#agenda.mostrar_eventos()
#agenda.eliminar_evento(1) #elimino un evento con el id
agenda.mostrar_eventos()
agenda.exportar_a_csv("events.csv")
