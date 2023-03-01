from tkinter import Tk,Button,Frame,messagebox

#5. Funcion agregar mensajes
def mostrarMensaje():
    messagebox.showinfo("aviso:","presionaste el boton azul")
    messagebox.showerror("Error:","el proceso fallo con exito")
    print(messagebox.askokcancel("Pregunta","Elle jugo con tu corazon"))
    print(messagebox.askquestion("Pregunta rapida","¿eri gay?"))
    print(messagebox.askyesnocancel("HI","hola"))
    print(messagebox.askretrycancel("Que es esto!!!","no se que hago :v"))
    
#6. Funcion para agregar botones
def agregarBoton():
    btonVerde.config(text="+",bg="green",fg="white")
    btonNuevo = Button(seccion3,text="Nuevo")
    btonNuevo.pack()
    

#1. instanciamos el objeto ventana
ventana= Tk()
ventana.title("ejemplo de 3 frames")
ventana.geometry("600x400")

#2. agregamos los frames 
seccion1= Frame(ventana,bg="blue")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana,bg="red")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana,bg="black")
seccion3.pack(expand=True,fill='both')

#3. agregamos los botones
btonAzul= Button(seccion1,text="boton Azul",fg="blue",bg="black",command=mostrarMensaje)
btonAzul.place(x="60",y="60") 

btonAmarillo= Button(seccion2,text="boton Amarillo",fg="yellow",bg="blue")
btonAmarillo.grid(row= 1, column= 1)

btonNegro= Button(seccion2,text="boton negro",fg="white",bg="black")
btonNegro.grid(row= 0, column= 0)

btonVerde= Button(seccion3,text="boton verde",fg="green",bg="#800080",command=agregarBoton)
btonVerde.configure(height=2,width=10)
btonVerde.pack()

#4. pocicion de elementos

# llamamos al main
ventana.mainloop()