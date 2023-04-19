from tkinter import messagebox
import sqlite3 
import bcrypt


class controladorBD:
    
    def __init__(self):
        pass
    
    
        # se realizo la coneccion para usarla cuando sea necesario
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/Administrador/Desktop/github POO/POOs184DiegoH/tkinterSQLite/archivos/ferre.db")
            print("conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
             print("No se pudo conectar")
             
    # Metodo para insertar        
    def gardarMAT(self,nom,can):
        
        #1.- llamar a la conexion
        conx= self.conexionBD()
        
        #2.- revisar que los parametros no estan vacios
        if(nom == "" or can == ""):
            messagebox.showwarning("cuidadito!!", "falta informacion")
            conx.close()
        else:
            #3.- prepara datos y el querySQL
            cursor= conx.cursor()
            datos=(nom,can)
            qrinsert="insert into MatConstruccion(Material,Cantidad) values(?,?)"
            
            #4.- proceder a insertar y cerramos conexion
            cursor.execute(qrinsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito"," Se guardo el material")
            
    def consulALL(self):
        conx= self.conexionBD()
    
        try:
                #4.- Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from MatConstruccion"
                
                #5.- Ejecucuion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSu= cursor.fetchall()
                conx.close()
                
                return RSu
            
        except sqlite3.OperationalError:
                print("error Consulta")
             
             
             