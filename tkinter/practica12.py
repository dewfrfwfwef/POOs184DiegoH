from tkinter import *
from validacion import validacion
from tkinter import ttk as ttk
from validacion import validacion
from tkinter import messagebox as Messagebox


def login():
    cor = Correo.get()
    pas= Contraseña.get()
    validacion.validacion(cor, pas)


#1. instanciamos el objeto ventana
ventana= Tk()   
ventana.geometry("600x400")
ventana.title("Login")

seccion1= Frame(ventana)
seccion1.pack(expand=True,fill='both')
 
seccion2= Frame(ventana)
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana)
seccion3.pack(expand=True,fill='both')

#texto para los campos
txtinicio= Label(seccion1,text="inicio de secion")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(width="650", height="80")

txtCorreo= Label(seccion2,text="correo:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=90,y=40)

txtContra= Label(seccion2,text="contraseña:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=300,y=40)

#los campos
Correo= Entry(seccion2, bg="#F3F3F3")
Correo.place(x=145, y=43)

Contraseña= Entry(seccion2, bg="#F3F3F3",show="*")
Contraseña.place(x=386, y=43)
print(Contraseña)

#3. agregamos los botones

btonloG= Button(seccion3,text="INGRESAR",fg="black",bg="white",command=login)
btonloG.configure(height=2,width=10)
btonloG.pack()



ventana.mainloop()