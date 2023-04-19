from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from clases import *

controlador= controladorBD()

def ejecutarInsert():
    controlador.gardarMAT(varNom.get(),varCan.get())
    print(varNom.get())
    print(varCan.get())
    
def MostrarMATS():
    mats= controlador.consulALL()

    for u in tree.get_children():
        tree.delete(u)
        
    for mat in mats:
        tree.insert("",END, values=(mat[0],mat[1],mat[2]))
        
def actualizarMAT():
    controlador.actualizarUsuario(varCha.get(),varCNom.get(),varCant.get())
    MostrarMATS()
    



ventana = Tk()
ventana.geometry("500x300")
ventana.title("CRU FERRETERIA")

panel= ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

blink1= ttk.Frame(panel)
blink2= ttk.Frame(panel)
blink3= ttk.Frame(panel)


#pestaña1: ingreasar mat
titulo= Label(blink1,text="Registro MATS",fg="blue",font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(blink1,text="material:").pack()
txtNom= Entry(blink1,textvariable=varNom).pack()

varCan= tk.StringVar()
lblCor= Label(blink1,text="cantidad:").pack()
txtCor= Entry(blink1,textvariable=varCan).pack()

btnGuard= Button(blink1,text="agregar",command=ejecutarInsert).pack()

#pestaña2: mostrar todos
titulo2= Label(blink2,text="Consultar Materiales",fg="green",font=("Modern",18)).pack()

colum= ('id','nombre','cantidad')

tree= ttk.Treeview(blink2, columns=colum,show='headings')

tree.heading('id',text='id')
tree.heading('nombre',text='nombre')
tree.heading('cantidad',text='cantidad')
tree.pack(fill="both")

btnShow= Button(blink2, text="Mostrar",command=MostrarMATS)
btnShow.pack()

#pestaña3: actualizar usuarios
titulo3= Label(blink3,text="Actualizar materiales",fg="green",font=("Modern",18)).pack()

varCha= tk.StringVar()
lblid= Label(blink3,text="identificador del material:").pack()
txtid= Entry(blink3,textvariable=varCha).pack()

varCNom= tk.StringVar()
lblNom= Label(blink3,text="nombre:").pack()
txtNom= Entry(blink3,textvariable=varCNom).pack()

varCant= tk.StringVar()
lblCor= Label(blink3,text="cantidad:").pack()
txtCor= Entry(blink3,textvariable=varCant).pack()

btnActualizar= Button(blink3,text="Actualizar",command=actualizarMAT).pack()

#titulos pestañas
panel.add(blink1,text="ingresar mats")
panel.add(blink2,text="mostrar mats")
panel.add(blink3,text="actualizar mats")


ventana.mainloop()