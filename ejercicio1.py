import random
#se eliminan espacios
print("**** Ciencias de la Computacion I - 2021")
print("**** Laboratorio 01 - Ejercicio #1 ****") #print no bien escrita
print()
nombre = input("Ingrese su nombre: ") #no se cerraron las comillas
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
x = len(nombre)
y = len(apellido) #apellido estaba mal definido
respuesta = (x * y * (random.randint(0, edad + 2) +  random.randint(0, edad + 10)))
print("Felicitaciones " + nombre + "!!!")
print("Ha ejecutado su primer programa en Python!")
print("Su respuesta para este programa es: " , respuesta)
print() #se agrego parentesis