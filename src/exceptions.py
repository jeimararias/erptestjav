import math

#while True: print("Hello world..")  #Syntax error

"""
x = 10 / 0              #ZeroDivisionError
y = 4 + saludo * 3      #NameError
z = '2' + 2             #TypeError
try:
    num1 = float(input("Ingrese numerador: "))
    num2 = float(input("Ingrese denominador: "))
except ValueError:
    print("Error: Los valores no son correctos")
"""

"""
try:
    num1 = float(input("Ingrese numerador: "))
    num2 = float(input("Ingrese denominador: "))
    div= num1 / num2

    if num1 < 0:
        raise TypeError("No se permiten numero negativos...")
except ZeroDivisionError:
    print("Error división por cero..")
except ValueError:
    print("Error: Los valores no son correctos")
except TypeError as ex:
    #print()
else:
    print("OK: Resultado: ",div)
"""

def calcularaiz(num1):
    if num1 < 0:
        raise ValueError("No se puede calcular raiz de numero negativo..")
    else:
        return( math.sqrt(num1))

try:
    op1 = float(input("Ingrese numero: "))
    print(calcularaiz(op1))
except ValueError as ex:
    print(ex)

print("programa terminado")


