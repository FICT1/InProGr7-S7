# 1. Suma de los primeros N números
# o Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los
# números desde 1 hasta N.
# o Especificación: Usa un bucle for y un acumulador.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sumar_numeros():
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            resultado = num1 + num2
        except ValueError:
            error = "Por favor ingresa solo números enteros válidos."
          

    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)


