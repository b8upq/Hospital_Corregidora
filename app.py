from flask import Flask, render_template, request, redirect
import controlador

# Instancia de Flask
app = Flask(__name__)

#La ruta raiz es la pagina de inicio (aqui se muestra el formulario)
@app.route('/')
def index():
    return render_template('Registro.html')
#La ruta /registro es la que recibe los datos del formulario y se comunica exclusivamente conn la platilla html 
# (ojo: la ruta /registro no se muestra en el navegador)
# (ojo: la ruta /registro debe estar conectada con el formulario HTML por medio del: form action="/registro")
@app.route('/registro', methods=['POST'])
def registro_pacientes():
    nombre = request.form['txtNombre']
    apellidopaterno = request.form['txtAP']
    apellidomaterno = request.form['txtAM']
    edad = request.form['txtEdad']
    controlador.registrar_persona(nombre, apellidopaterno, apellidomaterno, edad)
    return redirect('/')
    


# Usa el comando python app.py en la terminal para ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)

