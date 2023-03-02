# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, firstweekday="monday", selectmode='day', year=2023, month=1, day=1,
               background="black", disabledbackground="black", bordercolor="white",
               headersbackground="black", normalbackground="black", foreground='white',
               normalforeground='white', headersforeground='white', date_pattern="dd-mm-y")

cal.pack(pady=20)


def grad_date():
    dt_str = cal.get_date()
    dt = Calendar.datetime.strptime(dt_str, "%d-%m-%Y").date() #strptime convierte el str a formato date
    
    date.config(text="Selected Date is completed: " + dt_str)
    cal.calevent_create(date=dt, text='Hello World', tags= "Message")
    cal.tag_config("Message", background='red', foreground='yellow')


# Add Button and Label
Button(root, text="Complete Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Execute Tkinter
root.mainloop()