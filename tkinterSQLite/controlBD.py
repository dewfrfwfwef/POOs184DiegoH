from tkinter import messagebox
import sqlite3 
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    # se realizo la coneccion para usarla cuando sea necesario
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/Administrador/Desktop/github POO/POOs184DiegoH/tkinterSQLite/sql1.db")
            print("conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
             print("No se pudo conectar")
             
    # Metodo para insertar        
    def gardarUsuario(self,nom,cor,con):
        
        #1.- llamar a la conexion
        conx= self.conexionBD()
        
        #2.- revisar que los parametros no estan vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("cuidadito!!", "falta informacion")
            conx.close()
        else:
            #3.- prepara datos y el querySQL
            cursor= conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrinsert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
            
            #4.- proceder a insertar y cerramos conexion
            cursor.execute(qrinsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito"," Se guardo el usuario")
            
    def encriptarCon(self,con):
        conflat= con
        conflat= conflat.encode() #convertirno con a bytes
        sal = bcrypt.gensalt()
        conHa= bcrypt.hashpw(conflat,sal)
        print(conHa)
        return conHa
    
    def consultarUsuario(self,id):
        #1.- preparar conexion
        conx= self.conexionBD()
        #2.- verificar id no vacio
        if(id == ""):
            messagebox.showwarning("cuidado","id vacio ingrese un id")
            conx.close()
        else:
            #3.- proceder a buscar
            try:
                #4.- Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from TBRegistrados where id=" +id
                
                #5.- Ejecucuion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario= cursor.fetchall()
                conx.close()
                
                return RSusuario
            
            except sqlite3.OperationalError:
                print("error Consulta")
                
    def consulALL(self):
        conx= self.conexionBD()
    
        try:
                #4.- Preparar lo necesario para el select
                cursor= conx.cursor()
                sqlSelect="select * from TBRegistrados"
                
                #5.- Ejecucuion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSu= cursor.fetchall()
                conx.close()
                
                return RSu
            
        except sqlite3.OperationalError:
                print("error Consulta")
                
    def Delete(self,id):
        conx= self.conexionBD()
        if(id == ""):
            messagebox.showwarning("cuidado","id vacio ingrese un id")
            conx.close()
        else:
            try:
                cursor= conx.cursor()
                sqlDelete="delete from TBRegistrados where id=" +id
                pregunta = messagebox.askokcancel("adevertencia","Desea eliminar el usuario")
                if pregunta == True:
                    cursor.execute(sqlDelete)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito","se elimino el usuario")
                else:
                    conx.close()
                    messagebox.showinfo("Exito","No se elimino el usuario")
                
            except sqlite3.OperationalError:
                print("error Consulta")
                
    def actualizarUsuario(self,id,nom,cor,con):
            
            conx= self.conexionBD()
                
            if(id == "" or nom == "" or cor == "" or con == ""):
                messagebox.showwarning("cuidadito!!", "falta informacion")
                conx.close()
            else:
                try:
                    cursor= conx.cursor()
                    conH=self.encriptarCon(con)
                    datos=(nom,cor,conH,id)
                    qrUpdate="update TBRegistrados set nombre=?,correo=?,contra=? where id=?"
                        
                    cursor.execute(qrUpdate,datos)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito"," Se actualizo el usuario")
                        
                except sqlite3.OperationalError:
                    print("error Consulta")