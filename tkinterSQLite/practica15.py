from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from controlBD import *

# crear una istancia de tipo controlador
controlador= controladorBD()

#Proseder a guardar usuario 
def ejecutarInsert():
    controlador.gardarUsuario(varNom.get(),varCor.get(),varPas.get())


#Proseder a Buscar Usuario
def ejecutaSelectU():
    rsUsuario=  controlador.consultarUsuario(varBus.get())

    for usu in rsUsuario:
        cadena= str(usu[0])+" " + usu[1]+" " + usu[2]+" " + str(usu[3])
    
    if(rsUsuario):
        textBus.insert(tk.INSERT, cadena)
        print(cadena)
    else:
        messagebox.showinfo("no encontrado","Usuario no registrado en BD")
        
    return cadena
                

ventana = Tk()
ventana.geometry("500x300")
ventana.title("CRUD Usuarios")

panel= ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

blink1= ttk.Frame(panel)
blink2= ttk.Frame(panel)
blink3= ttk.Frame(panel)
blink4= ttk.Frame(panel)
#pestaña1: Formulario
titulo= Label(blink1,text="Registro Usuarios",fg="blue",font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(blink1,text="nombre:").pack()
txtNom= Entry(blink1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(blink1,text="correo:").pack()
txtCor= Entry(blink1,textvariable=varCor).pack()

varPas= tk.StringVar()
lblPas= Label(blink1,text="contraseña:").pack()
txtPas= Entry(blink1,textvariable=varPas).pack()

btnGuard= Button(blink1,text="Buscar Usuario",command=ejecutarInsert).pack()

#pestaña2: Buscar Usuario
titulo2= Label(blink2,text="Registro Usuarios",fg="green",font=("Modern",18)).pack()

varBus= tk.StringVar()
lblid= Label(blink2,text="identificador de usuario:").pack()
txtid= Entry(blink2,textvariable=varBus).pack()
btnBuscar= Button(blink2,text="Buscar",command=ejecutaSelectU).pack()


  
 
subBus= Label(blink2,text="Registro Usuarios",fg="blue",font=("Modern",15)).pack()
textBus= tk.Text(blink2,height=2,width=52)



textBus.pack()


#pestaña3: Formulario
#pestaña4: Formulario





panel.add(blink1,text="formulario de usuarios")
panel.add(blink2,text="Buscar Usuario")
panel.add(blink3,text="consultar usuarios")
panel.add(blink4,text="actualizar usuarios")

ventana.mainloop()