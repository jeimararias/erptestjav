#Smallest positive integer in a List

def solution(A):
	max_n=max(A)
	if max_n <= 0:
		max_n = 1
	max_n += 2

	print ("maximo: ", max_n)
	for i in range(1, max_n):
		#print("Ingrese: ",i)
		if i not in (A):
			break
	return i

miLista=[1, 3, 6, 4, 1, 2]
print("Must be 5: number = ",solution(miLista))
#print("Maximo en la lista: ",max(miLista))
print("Must be 4: number = ",solution([1, 2, 3]))
miLista=[-1, -3]
print("Must be 1: number = ",solution(miLista))


