from flask import Flask, render_template

app = Flask(__name__)

# Sintaxis basica para crear una ruta
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro_pacientes():
    return render_template('Registro.html')


# Usa el comando python app.py en la terminal para ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
