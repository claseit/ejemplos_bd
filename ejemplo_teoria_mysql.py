import pymysql

personas = (("oscar", 30),("Ernesto", 41),("Osvaldo", 27))

conn = pymysql.connect(host="host", port=3306, user="usuario_admin", passwd="clave_admin", db="nombre_bd")

cursor = conn.cursor()

idi = 0

for nombre,edad in personas:
    cursor.execute("INSERT INTO personas VALUES (%s, %s, %s)", (idi, nombre, edad))
    idi = idi + 1

conn.commit()
 
conn.close()

print("¡Datos ingresados correctamente!")