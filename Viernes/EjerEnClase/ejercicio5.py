#pedir contraseña y comprobar si es correcta
import os
clave = "1234"
intentos = 0
while intentos < 4:
    os.system("cls")
    clave_usuario = input("Introduce la contraseña: ")
    if clave_usuario == clave:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        intentos += 1
if intentos == 4:
    print("Has agotado los intentos")
