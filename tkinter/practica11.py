from tkinter import Tk,Button,Frame,messagebox

def mostrarMensaje():
    messagebox.showinfo("aviso:","presionaste el boton azul")

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

btonVerde= Button(seccion3,text="boton verde",fg="green",bg="#800080")
btonVerde.configure(height=2,width=10)
btonVerde.pack()


# llamamos al main
ventana.mainloop()