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
    print(varNom.get())
    print(varCor.get())
    print(varPas.get())


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

#eliminar usuarios
def eliminarUsu():
    controlador.Delete(varDel.get())
    MostrarUsus()


#Proseder a mostrar tabla de registros
def MostrarUsus():
    usus= controlador.consulALL()

    for u in tree.get_children():
        tree.delete(u)
        
    for usu in usus:
        tree.insert("",END, values=(usu[0],usu[1],usu[2],usu[3]))
     
#actualisar usuarios    
def actualizarUsu():
    controlador.actualizarUsuario(varCha.get(),varCNom.get(),varCCor.get(),varCPas.get())
    MostrarUsus()
    
                

ventana = Tk()
ventana.geometry("500x300")
ventana.title("CRUD Usuarios")

panel= ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

blink1= ttk.Frame(panel)
blink2= ttk.Frame(panel)
blink3= ttk.Frame(panel)
blink4= ttk.Frame(panel)
blink5= ttk.Frame(panel)

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

btnGuard= Button(blink1,text="agregar Usuario",command=ejecutarInsert).pack()

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
titulo3= Label(blink3,text="Consultar Usuarios",fg="green",font=("Modern",18)).pack()

colum= ('id','nombre','correo','contraseña')

tree= ttk.Treeview(blink3, columns=colum,show='headings')

tree.heading('id',text='id')
tree.heading('nombre',text='nombre')
tree.heading('correo',text='correo')
tree.heading('contraseña',text='contraseña')
tree.pack(fill="both")

btnShow= Button(blink3, text="Mostrar",command=MostrarUsus)
btnShow.pack()

#pestaña4: Eliminar
titulo3= Label(blink4,text="Eliminar Usuarios",fg="green",font=("Modern",18)).pack()

varDel= tk.StringVar()
lblid= Label(blink4,text="identificador de usuario:").pack()
txtid= Entry(blink4,textvariable=varDel).pack()
btnDelete= Button(blink4,text="eliminar",command=eliminarUsu).pack()

#pestaña5: actualizar usuarios
titulo4= Label(blink5,text="Actualizar Usuarios",fg="green",font=("Modern",18)).pack()

varCha= tk.StringVar()
lblid= Label(blink5,text="identificador de usuario:").pack()
txtid= Entry(blink5,textvariable=varCha).pack()

varCNom= tk.StringVar()
lblNom= Label(blink5,text="nombre:").pack()
txtNom= Entry(blink5,textvariable=varCNom).pack()

varCCor= tk.StringVar()
lblCor= Label(blink5,text="correo:").pack()
txtCor= Entry(blink5,textvariable=varCCor).pack()

varCPas= tk.StringVar()
lblPas= Label(blink5,text="contraseña:").pack()
txtPas= Entry(blink5,textvariable=varCPas).pack()

btnActualizar= Button(blink5,text="Actualizar",command=actualizarUsu).pack()

#titulos pestañas
panel.add(blink1,text="formulario de usuarios")
panel.add(blink2,text="Buscar Usuario")
panel.add(blink3,text="consultar usuarios")
panel.add(blink4,text="eliminar ususario")
panel.add(blink5,text="actualizar usuarios")

ventana.mainloop()