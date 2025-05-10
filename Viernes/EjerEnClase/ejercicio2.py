#imprimir cada letra de una palabra y dejar las vocales en mayusculas
import os 
os.system("cls")
vocales = "aeiou"
print("Imprimir cada letra de una palabra y dejar las vocales en mayusculas")
palabra = input("Introduce una palabra: ")
for letra in palabra:
    if letra.lower() in vocales:
        print(letra.upper(), end="")
    else:
        print(letra.lower(), end="")
