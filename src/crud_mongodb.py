from pymongo import MongoClient # El cliente de MongoDB
from producto import Producto # La clase Producto
from bson.objectid import ObjectId  #Para crear ObjectId, porque _id como cadena no funciona

def obtener_bd():
    host = "localhost"
    puerto = "27017"
    usuario = "user123"
    palabra_secreta = "pass123"
    base_de_datos = "mydatabase"
    #cliente = MongoClient("mongodb://{}:{}@{}:{}".format(usuario, palabra_secreta, host, puerto))
    cliente = MongoClient('mongodb://localhost:27017/')

    return cliente[base_de_datos]

def insertar(producto):
    base_de_datos = obtener_bd()
    productos = base_de_datos.productos
    return productos.insert_one({
        "nombre": producto.nombre,
        "precio": producto.precio,
        "cantidad": producto.cantidad,
        }).inserted_id

def obtener():
    base_de_datos = obtener_bd()
    return base_de_datos.productos.find()

def actualizar(id, producto):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad,
            }
        })
    return resultado.modified_count

def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count

def query_adhoc(query):
    print("Obteniendo resultados..\n")
    #myclient = MongoClient("mongodb://localhost:27017/")
    #mydb = myclient["mydatabase"]

    base_de_datos = obtener_bd()
    mycol = base_de_datos["productos"]
    #productos = base_de_datos.productos

    #mydoc = mycol.find(query).sort("nombre", -1)
    mydoc = mycol.find(query).sort("nombre", -1).limit(5)   #limit maxima cantidad de registros a traer

    for x in mydoc:
        print(x)

creditos = """==========================================================
	                CRUD de MongoDB y Python
                                           
                                __ __          __         
	.-----.---.-.----.-----|__|  |--.--.--|  |_.-----.
	|  _  |  _  |   _|-- __|  |  _  |  |  |   _|  -__|
	|   __|___._|__| |_____|__|_____|___  |____|_____|
	|__|                            |_____|           
=========================================================="""

menu = """Bienvenido a la tienda.
1 - Insertar producto
2 - Ver todos
3 - Actualizar
4 - Eliminar
5 - Salir
9 - Consulta Adhoc
"""
eleccion = None
print(creditos)
while eleccion is not 5:
    print(menu)
    eleccion = int(input("Elige: "))
    if eleccion is 1:
        print("Insertar")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = float(input("Cantidad del producto: "))
        producto = Producto(nombre, precio, cantidad)
        id = insertar(producto)
        print("El id del producto insertado es: ", id)
    elif eleccion is 2:
        print("Obteniendo productos...")
        for producto in obtener():
            print("=================")
            print("Id: ", producto["_id"])
            print("Nombre: ", producto["nombre"])
            print("Precio: ", producto["precio"])
            print("Cantidad: ", producto["cantidad"])
    elif eleccion is 3:
        print("Actualizar")
        id = input("Dime el id: ")
        nombre = input("Nuevo nombre del producto: ")
        precio = float(input("Nuevo precio del producto: "))
        cantidad = float(input("Nueva cantidad del producto: "))
        producto = Producto(nombre, precio, cantidad)
        productos_actualizados = actualizar(id, producto)
        print("Número de productos actualizados: ", productos_actualizados)
    elif eleccion is 4:
        print("Eliminar")
        id = input("Dime el id: ")
        productos_eliminados = eliminar(id)
        print("Número de productos eliminados: ", productos_eliminados)
    elif eleccion is 9:
        #myquery = { "nombre": { "$regex": "^z" } }
        stringToFind = input("Ingrese string a buscar: ")
        myquery = { "nombre": { "$gt": stringToFind } }
        query_adhoc(myquery)
