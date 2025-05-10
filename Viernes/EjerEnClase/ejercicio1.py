#sumar los primeros 10 numeros naturales usando un bucle for
import os 
os.system("cls")
suma = 0
expresion = ""
for i in range(1, 11):
    suma += i
    expresion += str(i)
    if i < 10:
        expresion += "+"
    print(f"La suma de {i} es: {suma}", )
print(f"\nExpresion: {expresion} = {suma}")

