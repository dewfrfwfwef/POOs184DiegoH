from tkinter import *
from control14 import *
from tkinter import messagebox
banc = banco()
def ingresar():
    def ingreso():
        cant = int(cantidad.get())
        banc.ingreso(cant)
    
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
        banc.retiro(cant)
    
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
    def depo():
        cuen = cuenta.get()
        cant = int(cantidad.get())
        banc.deposito(cuen,cant)
    
    ventana = Tk()
    ventana.geometry("400x400")
    ventana.title("ingresar dinero")
    
    txtcantidad= Label(ventana,text="No.cuenta:",fg="black")
    txtcantidad.configure(font=("calibri",13))
    txtcantidad.place(x=90,y=40)
    
    cuenta= Entry(ventana, bg="#F3F3F3")
    cuenta.place(x=165, y=43)
    
    txtcantidad= Label(ventana,text="cantidad:",fg="black")
    txtcantidad.configure(font=("calibri",13))
    txtcantidad.place(x=90,y=80)
    
    cantidad= Entry(ventana, bg="#F3F3F3")
    cantidad.place(x=165, y=83)
    
    btonloG= Button(ventana,text="depostar",fg="black",bg="white",command=depo)
    btonloG.place(x=195,y=120)
    
    btonloG= Button(ventana,text="cancelar",fg="black",bg="white",command=ventana.destroy)
    btonloG.place(x=195,y=160)
    
def consul():
    banc.datos()
    



#1. instanciamos el objeto ventana
ventana= Tk()   
ventana.geometry("600x400")
ventana.title("Login")

seccion1= Frame(ventana)
seccion1.config(background="#BB8FCE")
seccion1.pack(expand=True,fill='both')

#texto para los campos
txtinicio= Label(seccion1,text="banco xd",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=260,y=40)

txtinicio= Label(seccion1,text="que desea hacer:",bg="#BB8FCE")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=100,y=80)
#3. agregamos los botones
btonloG= Button(seccion1,text="consultar saldo",fg="white",bg="#4A235A",command=consul)
btonloG.place(x=130,y=110)

btonloG= Button(seccion1,text="retirar",fg="white",bg="#4A235A",command=retirar)
btonloG.place(x=130, y=140)

btonloG= Button(seccion1,text="ingreasar",fg="white",bg="#4A235A",command=ingresar)
btonloG.place(x=130, y=170)

btonloG= Button(seccion1,text="depositar",fg="white",bg="#4A235A",command=depositar)
btonloG.place(x=130, y=200)



ventana.mainloop()