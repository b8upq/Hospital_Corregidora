from flask import Flask, render_template, request, redirect
import controlador

# Instancia de Flask
app = Flask(__name__)

#Sintaxis basica para crear una ruta
@app.route('/')
def index():
    return render_template('Registro.html')

@app.route('/registro', methods=['GET', 'POST'])
def index_registro():
    nombre = request.form['txtNombre']
    apellidopaterno = request.form['txtAP']
    apellidomaterno = request.form['txtAM']
    edad = request.form['txtEdad']
    controlador.registrar_persona(nombre, apellidopaterno, apellidomaterno, edad)
    return render_template('Registro.html')


# Usa el comando python app.py en la terminal para ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
