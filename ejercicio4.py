"""
Tres agricultores van a recoger manzanas de los arboles de su granja. Deciden que cada uno recogera por separado, y al terminar el dia, uniran todas las manzanas recogidas, y las repartiran de tal forma que todos reciban el mismo numero de manzanas. Si sobran manzanas despues de repartir, las guardaran para comerlas al dia siguiente (no se toman en cuenta para la reparticion).
Escriba un programa que determine el numero de manzanas que recibira un agricultor, dada la cantidad de manzanas que cada uno recoge, leyendo los datos del usuario (es decir la cantidad de manzanas que recogieron los tres agricultores) y desplegando el resultado.
"""
persona1 = int(input("Cuantas recogio el primer agricultor: "))
persona2 = int(input("Cuantas recogio el segundo agricultor: "))
persona3 = int(input("Cuantas recogio el tercer agricultor: "))
cantidad_recogida = persona1 + persona2 + persona3
resultado = cantidad_recogida // 3
sobras = cantidad_recogida % 3
print("Cada uno recibe: ", resultado)
print ("Sobran: ", sobras)