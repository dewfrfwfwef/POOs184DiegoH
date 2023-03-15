from tkinter import *
from ControlExam2 import *


#1. instanciamos el objeto ventana
ventana= Tk()   
ventana.geometry("600x400")
ventana.title("Login")

seccion1= Frame(ventana)
seccion1.config(background="#BB8FCE")
seccion1.pack(expand=True,fill='both')

#texto para los campos
txtinicio= Label(seccion1,text="EXAmen2doP",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=260,y=20)

txtinicio= Label(seccion1,text="ingrese nombre:",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=100,y=80)

name= Entry(seccion1, bg="#F3F3F3")
name.place(x=225, y=83)

txtinicio= Label(seccion1,text="ingrese Apellido pa:",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=100,y=120)

lastPa= Entry(seccion1, bg="#F3F3F3")
lastPa.place(x=240, y=123)

txtinicio= Label(seccion1,text="ingrese Apelido ma:",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=100,y=160)

lastMA= Entry(seccion1, bg="#F3F3F3")
lastMA.place(x=240, y=163)

txtinicio= Label(seccion1,text="ingrese Ano de nacimento:",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=100,y=200)

nace= Entry(seccion1, bg="#F3F3F3")
nace.place(x=290, y=203)

txtinicio= Label(seccion1,text="ingrese Carrera:",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=100,y=240)

carrera= Entry(seccion1, bg="#F3F3F3")
carrera.place(x=220, y=243)
#3. agregamos los botones
btonloG= Button(seccion1,text="ingresar",fg="white",bg="#4A235A")
btonloG.place(x=420,y=80)

btonloG= Button(seccion1,text="ingresar",fg="white",bg="#4A235A")
btonloG.place(x=420,y=120)

btonloG= Button(seccion1,text="ingresar",fg="white",bg="#4A235A")
btonloG.place(x=420,y=160)

btonloG= Button(seccion1,text="ingresar",fg="white",bg="#4A235A")
btonloG.place(x=420,y=200)

btonloG= Button(seccion1,text="ingresar",fg="white",bg="#4A235A")
btonloG.place(x=420,y=240)

btonloG= Button(seccion1,text="prueba",fg="white",bg="#4A235A")
btonloG.place(x=420,y=240)


nombre = name.get()
apellidoP = lastPa.get()
apellidom = lastMA.get()
año = nace.get()
carr = carrera.get()

main = exam(nombre,apellidoP,apellidom,año,carr)







ventana.mainloop()