from db import conexion_db

# Conexion de prueba
def registrar_persona(nombre, apellidopaterno, apellidomaterno, edad):
    conexion = conexion_db()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO personas(Nombre, ApellidoPaterno, ApellidoMaterno, Edad) VALUES(%s, %s, %s, %s)", 
                       (nombre, apellidopaterno, apellidomaterno, edad))
        conexion.commit()
        conexion.close()
        
        
# def registrar_persona(nombre, apellidopaterno, apellidomaterno, edad, sexo):
#     conexion = conexion_db()
#     with conexion.cursor as cursor:
#         cursor.execute("INSERT INTO personas(Nombre, ApellidoPaterno, ApellidoMaterno, Edad, Sexo) VALUES(%s, %s, %s, %s, %s)", 
#                        (nombre, apellidopaterno, apellidomaterno, edad, sexo))
#         conexion.commit()
#         conexion.close()

