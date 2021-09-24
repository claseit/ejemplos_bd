import sqlite3


#personas = (("Jorge",40),("Tomas",10),("Marisa",50))

conn = sqlite3.connect("comercio.sqlite")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE clientes (nombre TEXT, edad INT)")
    print("Bienvenido")
except sqlite3.OperationalError:
    print("Bienvenido nuevamente")


#for nombre,edad in personas:
#    cursor.execute("INSERT INTO clientes VALUES(?,?)",(nombre,edad))

cursor.execute("SELECT * FROM clientes")

datos = cursor.fetchall()

conn.commit()
conn.close()

for n in datos:
    print(n)

