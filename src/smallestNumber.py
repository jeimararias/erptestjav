#Smallest positive integer

def solution(A):
	#Find maximun positive integer
	#number=1
	#for n in A:
	#	if n > number:
	#		number = n
	#number += 1 
	print ("Max in list: ",number)

	#Find the smallest integer that is not in list
	#for i in range(1,number):
	for i in range(1,100000):
		#print ("i: ",i)
		if i not in (A):
			number = i
			print ("Ingrese: ",i, " number: ", number)
			break
	return number

print("Must be 5: number = ",solution([1, 3, 6, 4, 1, 2]))
print("Must be 4: number = ",solution([1, 2, 3]))
print("Must be 1: number = ",solution([-1, -3]))


