"""
1. BEGIN
2. GET cantidad
3. GET tasa_cambio
4. GET impuesto
5. conversion <-- cantidad * tasa_cambio
6. porcentaje <-- impuesto / 100
7. precio <-- conversion + (conversion * porcentaje)
8. total <-- precio DIV 5
8. OUTPUT total
9. END
"""
cantidad = int(input("Ingrese la cantidad: "))
tasa_cambio = float(input("Ingrese tasa de cambio: "))
impuesto = int(input("Ingrese el impuesto: "))
conversion = cantidad * tasa_cambio
porcentaje = impuesto / 100
precio = conversion + (conversion * porcentaje)
total = precio // 5
print ("El total es: ", total)