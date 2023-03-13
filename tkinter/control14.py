from tkinter import messagebox

class banco:
    def __init__(self):
        self.ADcuenta = "1213"
        self.varo = 400
    
    def ingreso(self,cantidad):
        self.varo = self.varo + cantidad
        messagebox.showinfo("aviso:","dinero ingresado con exito")
       
    def retiro(self,cantidad):
        self.varo = self.varo - cantidad
        messagebox.showinfo("aviso:","dinero retirado con exito")
        
    def datos(self):
        print(self.varo)
        
    def deposito(self,cuenta,cantidad):
        #adcuent = "12134505"
        if cuenta != self.ADcuenta:
            messagebox.showinfo("error:","la cuenta no existe")
            print("error")
        else:
            self.varo = self.varo - cantidad
            messagebox.showinfo("Aviso:","deposito realizado")
            print("exito")
            
            
        
        
    
