# Promedio de N calificaciones
# o Enunciado: Pide al usuario la cantidad N de calificaciones y luego solicita cada
# calificación. Calcula el promedio de las calificaciones ingresadas.
# o Especificación: Usa un bucle for para leer las calificaciones, un acumulador para la
# suma, y un contador para la cantidad.
import os
os.system("cls || clear")
import time
import datetime as dt
fecha = dt.date.today()
print("**Promedio de N calificaciones**")
cantidad = int(input("Introduce la cantidad de calificaciones\n-> "))
suma = 0
for i in range(cantidad):
    os .system("cls || clear")
    calificacion = float(input(f"Introduce la calificación {i + 1}\n-> "))
    time.sleep(0.2)
    continue
    suma += calificacion
promedio = suma / cantidad
os.system("cls || clear")
print("**Promedio de N calificaciones**")
print ("Calculando el promedio")
for count in range(10):
    puntos = "." * (count +1)
    porcentaje = (count + 1) * 10
    print(f"\rCalculando{puntos:<10} {porcentaje}%", end="")
    time.sleep(1)

print(f"\nEl promedio de las calificaciones es: {promedio}")
