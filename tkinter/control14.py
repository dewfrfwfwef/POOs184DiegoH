from tkinter import messagebox
varo = 0
class banco:
    
    def ingreso(cantidad):
        global varo
        total = varo + cantidad
        varo = + total
        print(varo)
        return varo
        
        
    def retiro(cantidad):
        global varo
        total = varo - cantidad
        varo = + total
        print(varo)
        return varo
    
    
    
