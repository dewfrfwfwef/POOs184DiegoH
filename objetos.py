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
especieV = input("escribe la especie del villanp: ")
nombreV = input("escribe el nombre del villano: ")
alturaV = float(input("escribe la altura del villano: "))
recargaV = int(input("cuantas balas recarga el villano: "))

#2. crear objeto de clase personaje

heroe= personaje(especieH,nombreH,alturaH)
villano= personaje(especieV,nombreV,alturaV)

#3. usar atributos

print("")
print("####### objeto heroe #")
print ("el personaje se llama: " + heroe.nombre)
print ("su especie es: " + heroe.especie)
print ("y su altura es de: " + str(heroe.altura))

heroe.correr(True)
heroe.lanzarGranadas()
heroe.reload(87)

print("")
print("####### objeto villano #")
print ("el personaje se llama: " + villano.nombre)
print ("su especie es: " + villano.especie)
print ("y su altura es de: " + str(villano.altura))

villano.correr(True)
villano.lanzarGranadas()
villano.reload(87)


