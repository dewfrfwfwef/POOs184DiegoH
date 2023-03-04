from tkinter import messagebox
class validacion:
#metodo
    def validacion (correo,password):
        admin = "gato@admin.org"
        passadmin = "gato123"
        print(correo,password)
        if(correo == admin and password == passadmin):
            messagebox.showinfo("Aviso:","Bienvenido")
        else:
            messagebox.showerror("Error:","DATOS INCORRECTOS")