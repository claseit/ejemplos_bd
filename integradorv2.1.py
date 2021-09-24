import pymysql
import claves
import os

def verificar(dato):
    while dato == "":
        print("Error, dato nulo")
        dato = input("Ingrese nuevamente: ")
    return dato


def convertir(valor):
    while True:
        try:
            valor = int(valor)
            break
        except ValueError:
            print("Error, solo numeros")
        valor = input("Ingrese nuevamente el valor: ")
    return valor



def guardar(n,c,cod):
    conn = pymysql.connect(host=claves.servidor, port=3306, user=claves.usuario, passwd=claves.clave, db=claves.nombre_base)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO productos VALUES(%s,%s,%s)",(cod,n,c))
    except:
        try:
            cursor.execute("CREATE TABLE productos (id INT, nombre TEXT, precio INT)")
            cursor.execute("INSERT INTO productos VALUES(%s,%s,%s)",(cod,n,c))
        except:
            print("¡La tabla ya existia! ERROR 200")
    conn.commit()
    conn.close()
    return True


def mostrar():
    conn = pymysql.connect(host=claves.servidor, port=3306, user=claves.usuario, passwd=claves.clave, db=claves.nombre_base)
    cursor = conn.cursor()
    datos = None
    try:
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        for n in datos:
            print(n[0],"-",n[1],"-",n[2])
    except:
        print("¡Error! No hay datos en la base de datos")
    


###########################

os.system("cls") 

while True:
    print("1 - Ingreso de producto")
    print("2 - Mostrar todos los productos")
    print("3 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Ingrese nombre del producto: ")
        nombre = verificar(nombre)
        precio = input("Ingrese precio del producto: ")
        precio = convertir(precio)
        cu = input("Ingrese codigo del producto: ")
        cu = convertir(cu)
        if guardar(nombre,precio,cu) :
            print("Los datos fueron guardados")
        else:
            print("¡Hay un error, no se guardo!")
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        print("Gracias por utilizar nuestro programa")
        break
    else:
        print("Error de opcion")
    input("Toque ENTER para continuar...")
    os.system("cls")        
