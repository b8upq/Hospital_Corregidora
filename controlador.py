from db import conexion_db

#Registro de personas
def registrar_persona(nombre, apellidopaterno, apellidomaterno, edad, sexo):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO personas(Nombre, ApellidoPaterno, ApellidoMaterno, Edad, Sexo) VALUES(%s, %s, %s, %s, %s)", 
                       (nombre, apellidopaterno, apellidomaterno, edad, sexo))
        conexion.commit()
        #Obtener el id_persona generado
        cursor.execute("SELECT LAST_INSERT_ID()")
        id_persona = cursor.fetchone()[0]
        # Insertar en la tabla pacientes
        cursor.execute("INSERT INTO pacientes(PersonaID) VALUES(%s)", (id_persona,))
        conexion.commit()
    
    conexion.close()

#Funcion para editar los datos de la persona en los consultorios
def editar_persona(persona_id, nombre, apellidopaterno, apellidomaterno, edad, sexo):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE personas SET Nombre=%s, ApellidoPaterno=%s, ApellidoMaterno=%s, Edad=%s, Sexo=%s WHERE PersonaID=%s", 
                       (nombre, apellidopaterno, apellidomaterno, edad, sexo, persona_id))
        conexion.commit()
    
    conexion.close()
        
#Funcion para extraer el ultimo paciente registrado
def extraer_paciente():
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        #Consulta para obtener el último registro de la tabla pacientes
        cursor.execute("""
            SELECT p.*, pe.Nombre, pe.ApellidoPaterno, pe.ApellidoMaterno, pe.Edad, pe.Sexo
            FROM pacientes p
            JOIN personas pe ON p.PersonaID = pe.PersonaID
            ORDER BY p.PacienteID DESC
            LIMIT 1
        """)
        ultimo_paciente = cursor.fetchone()
    
    conexion.close()
    return ultimo_paciente

#Funcion para extraer el medico correspondiente al consultorio    
def medico_correspondiente(medico_id):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT m.*, pe.Nombre, pe.ApellidoPaterno, pe.ApellidoMaterno, pe.Edad, pe.Sexo
            FROM medicos m
            JOIN personas pe ON m.PersonaID = pe.PersonaID
            WHERE m.MedicoID = %s
            LIMIT 1
        """, (medico_id))
        medico_correspondiente = cursor.fetchone()
        
    conexion.close()
    return medico_correspondiente

#Funcion para registrar el diagnostico del paciente
def registrar_diagnostico(paciente_id, medico_id, fecha_consulta, descripcion):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO diagnosticos(PacienteID, MedicoID, FechaConsulta, Descripcion) VALUES(%s, %s, %s, %s)", 
                       (paciente_id, medico_id, fecha_consulta, descripcion))
        conexion.commit()
    
    conexion.close()

