from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        tarros = int(request.form.get('tarros'))

        # Cálculos
        precio_unitario = 9000
        total_sin_descuento = tarros * precio_unitario

        # Aplicar descuento según la edad
        if edad < 18:
            descuento_aplicado = 0
        elif 18 <= edad <= 30:
            descuento_aplicado = total_sin_descuento * 0.15
        else:  # Edad > 30
            descuento_aplicado = total_sin_descuento * 0.25

        total_con_descuento = total_sin_descuento - descuento_aplicado

        # Resultado para mostrar en el formulario
        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento_aplicado,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == 'pepe':
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
