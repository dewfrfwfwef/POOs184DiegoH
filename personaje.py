class personaje:
    
    #definimos el constructor del personaje
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #metodo pesonaje
    def correr(self, estatus):
        if(estatus):
            print("el personaje " + self.__nombre + " esta corriendo")
        else:
            print("el personaje " + self.__nombre + " se detuvo")
        
    def lanzarGranadas(self):
        print("el personaje " + self.__nombre + " lanzo una granada")
    
    def reload(self, municion):
        cargador= 10
        cargador= cargador + municion
        print("el arma tiene " + str(cargador) + " balas")
        
    def __pensar(self):
        print("TOY pensando....")
    
    
    # declarar getters y setters de atributo

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre= nom
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie= esp
        
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura= alt