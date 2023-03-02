"""jam=hora,judul=titulo, tambah=grabar, hapus=borrar, waktu=horayminuto,keterngan detalle"""
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.scrolledtext import ScrolledText
from time import strftime
from tkinter import messagebox
from tkinter import *

to_dos = {}

def detallar_To_Do(cb=None):
    win = tk.Toplevel()
    win.wm_title('Calendario')
    itemseleccionado = treev.focus()
    indiceseleccionado = treev.item(itemseleccionado)['text'] #text es el indice de las actividades almacenadas
    eventoseleccionado = to_dos[fecha][indiceseleccionado]
    titulo = tk.StringVar(value=eventoseleccionado['Titulo'])
    tk.Label(win, text='fecha:').grid(row=0, column=0, sticky='N')
    tk.Label(win, text='{} | {}'.format(fecha, eventoseleccionado['horayminuto'])).grid(row=0, column=1, sticky='E')
    tk.Label(win, text='titulo:').grid(row=1, column=0, sticky='N')
    tk.Entry(win, state='disabled', textvariable=titulo).grid(row=1, column=1, sticky='E')
    tk.Label(win, text='detalle:').grid(row=2, column=0, sticky='N')
    detalle = ScrolledText(win, width=12, height=5)
    detalle.grid(row=2, column=1, sticky='E')
    detalle.insert(tk.INSERT, eventoseleccionado['detalle'])
    detalle.configure(state='disabled', bg="#7FFFD4")    

def guardar_to_do():
    f = open('MyTodo.txt','w')
    f.write(str(to_dos))
    f.close()

def cargar_to_do():
    global to_dos
    f = open('MyTodo.txt','r')
    data = f.read()
    f.close()
    to_dos = eval(data) #con eval los datos de la cadena se convierten en un dict
    Listar_to_do()
    
def mensaje_borrar():
    response = messagebox.askquestion("Advertencia!")
    if response == "yes":
        selectedItem = treev.focus()
        fecha = str(cal.selection_get())
        to_dos[fecha].pop(treev.item(selectedItem)["text"])
        Listar_to_do()  

"""
def delTodo():
    fecha = str(cal.selection_get())
    selectedItem = treev.focus() #akan mendapatkan index dari item yang diklik di treeview
    todos[fecha].pop(treev.item(selectedItem)['text'])
    ListTodo()
#pop berguna untuk mengborrar item
"""
    
def Listar_to_do(cb=None):
    for i in treev.get_children():
        treev.delete(i)
    fecha = str(cal.selection_get())
    if fecha in to_dos:
        for i in range(len(to_dos[fecha])):
            treev.insert('','end', text=i, values=(to_dos[fecha][i]['titulo'], to_dos[fecha][i]['horayminuto']))


def add_to_do(win, clave, hora, minuto, titulo, detalle):
    new_to_do = {
        'horayminuto':'{}:{}'.format(hora.get(), minuto.get()),
        'titulo': titulo.get(),
        'detalle': detalle.get('1.0', tk.END) #extraer detalles desde la primera linea hasta la ultima
    }
    if clave in to_dos:
        to_dos[clave].append(new_to_do)
    else:
        to_dos[clave] = [new_to_do]
    win.destroy()
    Listar_to_do()

def AddForm():
    win = tk.Toplevel()
    win.wm_title('+')
    Hora = tk.IntVar(value=10) #convierto en entero la hora
    menit = tk.IntVar(value=30) #convierto en entero los minutos
    titulo = tk.StringVar(value='')
    tk.Label(win, text='horayminuto: ', font="Garamond 12").grid(row=0, column=0)
    tk.Spinbox(win, from_=0, to=23, textvariable=Hora, font="Garamond 12",
            width=3, bg="#C32148", fg="white").grid(row=0, column=1)
    tk.Spinbox(win, from_=0, to=59, textvariable=menit, font="Garamond 12",
            width=3, bg="#FF007F", fg="white").grid(row=0, column=2)
    tk.Label(win, text='titulo: ', font="Garamond 12").grid(row=1, column=0)
    tk.Entry(win, textvariable=titulo, font="Garamond 12", 
            bg="#E7FEFF").grid(row=1, column=1, columnspan=2)
    tk.Label(win, text='Detalle', font="Garamond 12").grid(row=2, column=0)
    detalle = ScrolledText(win, width=12, height=5, font="Garamond 12",
                            bg="#89CFF0")
    detalle.grid(row=2, column=1, columnspan=2, rowspan=4)
    fecha = str(cal.selection_get())
    tk.Button(win, text='grabar', font="Garamond 12", command = lambda: add_to_do(win, fecha, Hora, 
            menit, titulo, detalle), bg="#013220", fg="white").grid(row=6, column=1)


def title():
  #  global cal
    horayminuto = strftime('%H:%M')
    fecha = str(cal.selection_get())
    root.title(fecha + " | " + horayminuto + " | krypto Calendar")
    root.after(1000,title)

root = tk.Tk()
root.title('Kalenderku')
root.configure(background="#A3C1AD")
style = ttk.Style(root)
style.theme_use("clam")
style.configure('Treeview', font="Garamond 11", rowheight=16, fieldbackground="#EDC9AF")

my_menu=Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=guardar_to_do)
file_menu.add_command(label="Load", command=cargar_to_do)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="grabar", command=AddForm)
edit_menu.add_command(label="borrar", command=mensaje_borrar)

cal = Calendar(root, font='Broadway 16', selectmode='day', locale='id_ID', cursor='pirate')
cal.pack(pady=20, fill="both", expand=True)
cal.grid(row=0, column=3, sticky='WNE', rowspan=7)
cal.bind('<<CalendarSelected>>', Listar_to_do) #Jika memilih fecha yang berbeda, akan memanggil ListTodo
cal.configure(background="#FF6961", foreground="#FFB7C5", bordercolor="white", borderwidth=6,
            normalbackground="#FF6961", normalforeground="#FFB7C5",
            headersbackground="#FFB7C5", headersforeground="#FF6961", 
            selectbackground="#FFB7C5", selectforeground="#FF6961",
            othermonthbackground="#DE5D83", othermonthforeground="#E7FEFF", weekendbackground="#CD5C5C",
            weekendforeground="white", othermonthwebackground="#DE3163",
            othermonthweforeground="#E7FEFF", showweeknumbers=False)

fecha = str(cal.selection_get())

treev = ttk.Treeview(root)
treev.grid(row=0, column=0, sticky='WNE', rowspan=4, columnspan=2)
scrollBar = tk.Scrollbar(root, orient='vertical', command=treev.yview)
#artinya, scrollbar yang dibuat disini berfyungsi untuk mengatur posisi y (vertikal)
#atau atas bawah, seperti sb.y pada diagram kartesius
scrollBar.grid(row=0, column=2, sticky='ENS', rowspan=4)
#ens untuk memposisikan di pojok kanan dan ada di treeview

treev.configure(yscrollcommand=scrollBar.set)
treev.bind('<Double-1>', detallar_To_Do) #membinding tombol klik kiri sebanyak 2 kali (double klik) dan memanggil detail todo
treev['columns'] = ('1', '2')
treev['show'] = 'headings'
treev.column('2', width=100)
treev.heading('2', text='Hora')
treev.heading('1', text='titulo')


#Adding button
btnAdd = tk.Button(root, text='grabar', width=16, command=AddForm, font="Broadway 11", 
                bg="#E52B50", fg="white")
btnAdd.grid(row=4, column=0, sticky='N')

btnDel = tk.Button(root, text='borrar', width=16, command=mensaje_borrar, font="Broadway 11", 
                bg="#FFEF00")
btnDel.grid(row=6, column=0, sticky='N')

btnLoad = tk.Button(root, text='Load', width=16, command=cargar_to_do, font="Broadway 11",
                bg="#A4C639", fg="white")
btnLoad.grid(row=6, column=1, sticky='N')

btnSave = tk.Button(root, text='Save', width=16, command=guardar_to_do, font="Broadway 11",
                bg="#318CE7")
btnSave.grid(row=4, column=1, sticky='N')

title()
root.mainloop()