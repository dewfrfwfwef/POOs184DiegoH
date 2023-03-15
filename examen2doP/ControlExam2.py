from tkinter import messagebox

class exam:
    def __init__(self,nombre,apellidoP,apellidoM,año,carrera):
        self.name = nombre
        self.lastP = apellidoP
        self.lastM = apellidoM
        self.año = año
        self.carrera = carrera
        
    def nombre(self,nombre):
        self.name = nombre
        print (self.name)