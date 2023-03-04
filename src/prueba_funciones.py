import random

def len_string(A):
	i=0
	for j in (A):
		i += 1
	return i

def sumar(A):
	result=0
	for j in (A):
		result += j
	return result

def multiplicar(A):
	if len(A) == 0:
		return 0
	result=1	
	for j in (A):
		result *= j
		#print(result)
	return result

def inversa_string(A):
	j=0
	inv_str = ""
	for i in range(len(A)-1,-1,-1):
		#print(A[i])
		inv_str += A[i]
	return inv_str	

def histograma(A):
	for i in (A):
		print("*"*i)

def nMayusculas (S):
	n=0
	for l in S:
		if l.isalpha() and l.isupper():
			n += 1
	return n

def nEdades(A, x):
	n=0
	for i in (A):
		if i > x:
			n += 1
			#print("i=",i,"  n=",n)
	return n

def es_bisiesto(anio):
	es_bis = False
	if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
		es_bis = True
	return es_bis

def adivinar_string(A, N):
	if A==N:
		print("Adivinaste el numero !!!", A)
		return True
	i=0
	num=0
	for d in (A):
		if d == N[i]:
			num += 1
		i+=1
	print ("Haz adivinado: ",num, " numeros")
	return False

def Future_Value(C,i,n):
	return C*(1+i/100)**n

#valor=Future_Value(10000,4.5,20)
#print("VF= ",valor)

#print("La longitud de ", len_string("Jeimar Arias"))
#print("La suma es ", sumar([1,2,3,4]))
#r=multiplicar([-1,20])
#print("La multiplicacion es ", r)
#print("La cadena inversa es: ", inversa_string("Jeimar Arias"))
#histograma([4,9,7])
#print(nMayusculas("JeiMar2021& AriaS VéleZ"))
#print("Total edades >",nEdades((1,21,20,15,25),20))
#ano = int(input("Ingrese año:"))
#print ("Es bisiesto el año: ",ano," result= ", es_bisiesto(ano))

""" comentareado desde aqui:  Llamado al numero
long=int(input("Digite longitud: "))

aleatorio=""
for i in range(long):
	a =  random.randint(0, 9)
	aleatorio += str(a)

print("Numero aleatorio: ",aleatorio)
intentos=0
while True:
	num=input("Digite numero de {} cifras: ".format(long))
	adivinar=adivinar_string(aleatorio, num)
	intentos += 1
	if intentos >= 3 or adivinar:
		break

 hasta aqui.."""




#*** Funciones ***
#s.find("world")
#s.startswith("Hola")
#s.endswith("mundo")
#"1234".isnumeric()
#"abc123".isalnum()
#"abcdef".islower()
#"hola mundo".capitalize()
#s = " Hola mundo! "; s.strip()
#s = "Hola mundo"; s.replace("mundo", "world")
#"Hola mundo!\nHello world!".split()

