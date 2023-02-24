from personaje import *

#.1 solicitar datos
print("")
print("####### datos heroe #")
especieH = input("escribe la especie del heroe: ")
nombreH = input("escribe el nombre del heroe: ")
alturaH = float(input("escribe la altura del heroe: "))
recargaH = int(input("cuantas balas recarga el heroe: "))

print("")
print("####### datos villano #")
especieV = input("escribe la especie del villano: ")
nombreV = input("escribe el nombre del villano: ")
alturaV = float(input("escribe la altura del villano: "))
recargaV = int(input("cuantas balas recarga el villano: "))

#2. crear objeto de clase personaje

heroe= personaje(especieH,nombreH,alturaH)
villano= personaje(especieV,nombreV,alturaV)

#3. usar atributos

#ejemplo set para un atributo
heroe.setNombre(" Pepe pecas ")

print("")
print("####### objeto heroe #")
print ("el personaje se llama: " + heroe.getNombre())
print ("su especie es: " + heroe.getEspecie())
print ("y su altura es de: " + str(heroe.getAltura()))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.reload(30)

#ejemplo metodo priv
#heroe.__pensar()

print("")
print("####### objeto villano #")
print ("el personaje se llama: " + villano.getNombre())
print ("su especie es: " + villano.getEspecie())
print ("y su altura es de: " + str(villano.getAltura()))

villano.correr(False)
villano.lanzarGranadas()
villano.reload(64)


