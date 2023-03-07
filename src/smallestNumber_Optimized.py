#Smallest positive integer in a List

def solution(A):
	A.sort()  # Ordena para mayor facilidad
	for i in range(1, 100001):
		if i not in (A):
			break
	return i

miLista=[1, 3, 6, 4, 1, 2]
print("Must be 5: number = ",solution(miLista))
#print("Maximo en la lista: ",max(miLista))
print("Must be 4: number = ",solution([1, 2, 3]))
miLista=[-1, -3]
print("Must be 1: number = ",solution(miLista))


