import pymysql #Requiere instalar el paquete pymysql con: pip install pymysql

def conexion_db():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='hospital_corregidora')   