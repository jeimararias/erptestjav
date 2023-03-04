import random

def tasa_descuento (Monto):
    trade_off = 0
    if Monto < 100:
        a =  random.randint(0, 4)
        if a == 0:
            trade_off = 0
            print("BOLA BLANCA. No tiene descuento: {}%".format(trade_off))
        elif a == 1:
            trade_off = 10
            print("BOLA ROJA. Descuento: {}%".format(trade_off))
        elif a == 2:
            trade_off = 20
            print("BOLA AZUL. Descuento: {}%".format(trade_off))
        elif a == 3:
            trade_off = 25
            print("BOLA VERDE. Descuento: {}%".format(trade_off))
        else:
            trade_off = 50
            print("BOLA AMARILLA. Descuento: {}%".format(trade_off))
    else:
        print("Monto superior a $100. No tienes descuento")
    return trade_off

### Mensaje
def lista_productos(p):
    print ("ELIJA EL PRODUCTO DESEADO\n")
    print ("Cod.PRODUCTO   PRECIO\n")
    print("Nombre producto: ",p[3][0])
    for i in range(1,11):   #el ultimo no lo genera
        print("{}.{}..........{}".format(i,p[i][0],p[i][1]))

#Uso de dictionarios#
productos={1:["CAMISA",35], 2:["CINTURON",10], 3:["ZAPATOS",50], 4:["PANTALON",40], 5:["CALCETINES",5], 6:["FALDAS",20], 7:["GORRAS",7], 8:["SUETER",15], 9:["CORBATA",10], 10:["CHAQUETA",35]}

monto_total=0.0
while True:
    lista_productos(productos)
    cod_p=int(input("Ingrese codigo de 1 a 10: "))
    print("El articulo escogido es {}... Costo unitario: {}".format(productos[cod_p][0],productos[cod_p][1]))
    cantidad=float(input("Ingrese cantidad : "))
    valor_articulo = cantidad * productos[cod_p][1]
    monto_total += valor_articulo
    print("Total articulo: ",valor_articulo, "  Monto acmulado: ", monto_total)
    y=input("Desea ingresar mas articulos: y/n").lower()
    if y not in ["y","s"]:
        break

print("*** Monto TOATAL: ", monto_total)


#dictionary={1:35, 2:10, 3:50, 4:40, 5:5, 6:20, 7:7, 8:15, 9:10, 10:35}

""" Ejecucion del monto a pagar
monto_base=float(input("Digite el monto de compra: "))
descuento = tasa_descuento (monto_base)
monto_final = monto_base * (1 - descuento / 100)
print("El monto a pagar es: ", monto_final)
"""
