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
    sexo = request.form['txtSexo']
    consultorio = request.form['txtConsultorio']
    controlador.registrar_persona(nombre, apellidopaterno, apellidomaterno, edad, sexo)
    
    if consultorio == '1':
        return redirect('/consultorio/1')
    elif consultorio == '2':
        return redirect('/consultorio/2')
    elif consultorio == '3':
        return redirect('/consultorio/3')
    
#####################################################################################################
##################################Seccion exclusiva para el consultorio 1
#Se declara la ruta para el consultorio 1
@app.route('/consultorio/1')
def consultorio1():
    ultimo_paciente = controlador.extraer_paciente()
    medico_correspondiente = controlador.medico_correspondiente(1) #El 1 es el id del medico(EL QUE ESTA EN LA BASE DE DATOS)
    return render_template('consultorio1.html', ultimo_paciente=ultimo_paciente, medico_correspondiente=medico_correspondiente)

#Ruta para editar los datos del paciente
@app.route('/consultorio1', methods=['POST'])
def con1():
    ultimo_paciente = controlador.extraer_paciente()
    id_paciente = ultimo_paciente[1]
    nombre = request.form['txtNombre']
    apellidopaterno = request.form['txtAP']
    apellidomaterno = request.form['txtAM']
    edad = request.form['txtEdad']
    sexo = request.form['txtSexo']
    controlador.editar_persona(id_paciente, nombre, apellidopaterno, apellidomaterno, edad, sexo)
    return redirect('/consultorio/1')

#Ruta para registrar el diagnostico del paciente
@app.route('/diagnostico1', methods=['POST', 'GET'])
def diagnostico1():
    ultimo_paciente = controlador.extraer_paciente()
    id_paciente = ultimo_paciente[0]
    medico_correspondiente = controlador.medico_correspondiente(1)
    id_medico = medico_correspondiente[0]
    fecha_consulta = request.form['txtFecha']
    descripcion = request.form['txtDescripcion']
    enfermedad = request.form['txtEnfermedad']
    controlador.registrar_diagnostico(id_paciente, id_medico, fecha_consulta, descripcion, enfermedad)
    return redirect('/')

#####################################################################################################
##################################Seccion exclusiva para el consultorio 2
#Se declara la ruta para el consultorio 2
@app.route('/consultorio/2')
def consultorio2():
    ultimo_paciente = controlador.extraer_paciente()
    medico_correspondiente = controlador.medico_correspondiente(2) #El 2 es el id del medico(EL QUE ESTA EN LA BASE DE DATOS)
    return render_template('consultorio2.html', ultimo_paciente=ultimo_paciente, medico_correspondiente=medico_correspondiente)

@app.route('/consultorio2', methods=['POST'])
def con2():
    ultimo_paciente = controlador.extraer_paciente()
    id_paciente = ultimo_paciente[1]
    nombre = request.form['txtNombre']
    apellidopaterno = request.form['txtAP']
    apellidomaterno = request.form['txtAM']
    edad = request.form['txtEdad']
    sexo = request.form['txtSexo']
    controlador.editar_persona(id_paciente, nombre, apellidopaterno, apellidomaterno, edad, sexo)
    return redirect('/consultorio/2')

#Ruta para registrar el diagnostico del paciente
@app.route('/diagnostico2', methods=['POST', 'GET'])
def diagnostico2():
    ultimo_paciente = controlador.extraer_paciente()
    id_paciente = ultimo_paciente[0]
    medico_correspondiente = controlador.medico_correspondiente(2)
    id_medico = medico_correspondiente[0]
    fecha_consulta = request.form['txtFecha']
    descripcion = request.form['txtDescripcion']
    enfermedad = request.form['txtEnfermedad']
    controlador.registrar_diagnostico(id_paciente, id_medico, fecha_consulta, descripcion, enfermedad)
    return redirect('/')

#####################################################################################################
##################################Seccion exclusiva para el consultorio 3
#Se declara la ruta para el consultorio 3
@app.route('/consultorio/3')
def consultorio3():
    ultimo_paciente = controlador.extraer_paciente()
    medico_correspondiente = controlador.medico_correspondiente(3) #El 3 es el id del medico(EL QUE ESTA EN LA BASE DE DATOS)
    return render_template('consultorio3.html', ultimo_paciente=ultimo_paciente, medico_correspondiente=medico_correspondiente)

#Ruta para editar los datos del paciente
@app.route('/consultorio3', methods=['POST'])
def con3():
    ultimo_paciente = controlador.extraer_paciente()
    id_paciente = ultimo_paciente[1]
    nombre = request.form['txtNombre']
    apellidopaterno = request.form['txtAP']
    apellidomaterno = request.form['txtAM']
    edad = request.form['txtEdad']
    sexo = request.form['txtSexo']
    controlador.editar_persona(id_paciente, nombre, apellidopaterno, apellidomaterno, edad, sexo)
    return redirect('/consultorio/3')

#Ruta para registrar el diagnostico del paciente
@app.route('/diagnostico3', methods=['POST', 'GET'])
def diagnostico3():
    ultimo_paciente = controlador.extraer_paciente()
    id_paciente = ultimo_paciente[0]
    medico_correspondiente = controlador.medico_correspondiente(3)
    id_medico = medico_correspondiente[0]
    fecha_consulta = request.form['txtFecha']
    descripcion = request.form['txtDescripcion']
    controlador.registrar_diagnostico(id_paciente, id_medico, fecha_consulta, descripcion)
    return redirect('/')


# Usa el comando python app.py en la terminal para ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)

