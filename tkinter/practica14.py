from tkinter import *
from control14 import *


def ingresar():
    def ingreso():
        cant = int(cantidad.get())
        banco.ingreso(cant)
    
    ventana = Tk()
    ventana.geometry("400x400")
    ventana.title("ingresar dinero")
    
    txtcantidad= Label(ventana,text="deposito:",fg="black")
    txtcantidad.configure(font=("calibri",13))
    txtcantidad.place(x=90,y=40)
    
    cantidad= Entry(ventana, bg="#F3F3F3")
    cantidad.place(x=165, y=43)
    
    btonloG= Button(ventana,text="aceptar",fg="black",bg="white",command=ingreso)
    btonloG.place(x=195,y=80)
    
    btonloG= Button(ventana,text="cancelar",fg="black",bg="white",command=ventana.destroy)
    btonloG.place(x=195,y=110)
    
def retirar():
    def ret():
        cant = int(cantidad.get())
        banco.retiro(cant)
    
    ventana = Tk()
    ventana.geometry("400x400")
    ventana.title("ingresar dinero")
    
    txtcantidad= Label(ventana,text="retiro:",fg="black")
    txtcantidad.configure(font=("calibri",13))
    txtcantidad.place(x=90,y=40)
    
    cantidad= Entry(ventana, bg="#F3F3F3")
    cantidad.place(x=165, y=43)
    
    btonloG= Button(ventana,text="retirar",fg="black",bg="white",command=ret)
    btonloG.place(x=195,y=80)
    
    btonloG= Button(ventana,text="cancelar",fg="black",bg="white",command=ventana.destroy)
    btonloG.place(x=195,y=110)
    
def depositar():
    ventana = Tk()
    ventana.geometry("400x400")
    ventana.title("ingresar dinero")
    
    txtcantidad= Label(ventana,text="No.cuenta:",fg="black")
    txtcantidad.configure(font=("calibri",13))
    txtcantidad.place(x=90,y=40)
    
    cantidad= Entry(ventana, bg="#F3F3F3")
    cantidad.place(x=165, y=43)
    
    txtcantidad= Label(ventana,text="cantidad:",fg="black")
    txtcantidad.configure(font=("calibri",13))
    txtcantidad.place(x=90,y=80)
    
    cantidad= Entry(ventana, bg="#F3F3F3")
    cantidad.place(x=165, y=83)
    
    btonloG= Button(ventana,text="retirar",fg="black",bg="white")
    btonloG.place(x=195,y=120)
    
    btonloG= Button(ventana,text="cancelar",fg="black",bg="white",command=ventana.destroy)
    btonloG.place(x=195,y=160)
    

    



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
txtinicio= Label(seccion1,text="banco xd")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(width="650", height="80")


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

btonloG= Button(seccion3,text="consultar saldo",fg="black",bg="white")
btonloG.configure(height=2,width=10)
btonloG.pack()

btonloG= Button(seccion3,text="retirar",fg="black",bg="white",command=retirar)
btonloG.place(x=30, y=60)
btonloG.pack()

btonloG= Button(seccion3,text="ingreasar",fg="black",bg="white",command=ingresar)
btonloG.place(x=30, y=90)
btonloG.pack()

btonloG= Button(seccion3,text="depositar",fg="black",bg="white",command=depositar)
btonloG.place(x=30, y=90)
btonloG.pack()


ventana.mainloop()