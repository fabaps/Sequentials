"""
Escriba un programa en Python que lea del usuario un numero positivo (asuma que es asi, no tiene que hacer verificaciones), y despliegue dos numeros aleatorios entre 0 y ese numero. Para poder encontrar un numero entero aleatorio, puede la funcion random.randint().
"""
import random
numeropositivo = int(input("Ingrese un numero positivo: "))
respuesta1 = random.randint(0,numeropositivo)
respuesta2 = random.randint(0,numeropositivo)
print ("Los dos numeros aleatorios son : ", respuesta1, "y", respuesta2)