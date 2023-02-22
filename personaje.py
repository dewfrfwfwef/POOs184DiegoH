class personaje:
    
    #definimos el constructor del personaje
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    #metodo pesonaje
    def correr(self, estatus):
        if(estatus):
            print("el personaje " + self.nombre + " esta corriendo")
        else:
            print("el personaje " + self.nombre + " se detuvo")
        
    def lanzarGranadas(self):
        print("el personaje " + self.nombre + " lanzo una granada")
    
    def reload(self, municion):
        cargador= 10
        cargador= cargador + municion
        print("el arma tiene " + str(cargador) + " balas")
    
    