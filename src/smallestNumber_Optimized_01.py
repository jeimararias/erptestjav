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

def findShortestSubstringxx(s):
	sr=""
	maxl=len(s)
	for i in range(maxl):
		for j in range(i+1,maxl):
			if s[j] == s[i]:
				continue
			else:
				sr+=s[i]
				break
	return sr

def findShortestSubstring(s):
	sr=""
	maxl=len(s)
	i=0
	while i < maxl:
		if (i+1)==maxl:
			sr+=s[i]
			break
		if s[i] != s[i+1]:
			sr+=s[i]
			i+=1
		else:
			i+=2
	return sr

def minimalOperations(words):
	ac=[]
	j=0
	for word in words:
		mins=0
		i=0
		while i < len(word):
			if i+1 == len(word):
				break
			if word[i] == word[i+1]:
				i+=2
				mins+=1
			else:
				i+=1
		ac.append(mins)
		j+=1		
	return ac

def findLongestSubsequence(arr):
	arr.sort()
	for i in range(1,len(arr)):
		arr1 = []
		arr1.append(arr[0])
		dif=0
		for j in (i,len(arr)):
			arr1.append[arr[j]]
			dif+=arr1[j]-arr1[j-1]
			
	arr
	for i in 
	#print(arr)


arr = [2,4,1,7]
print(findLongestSubsequence(arr))


words = ["add","boook","break"]
#print (minimalOperations(words))
    # Write your code here


s="abcbbk"
#print(findShortestSubstring(s))




"""	
miLista=[1, 3, 6, 4, 1, 2]
print("Must be 5: number = ",solution(miLista))
#print("Maximo en la lista: ",max(miLista))
print("Must be 4: number = ",solution([1, 2, 3]))
miLista=[-1, -3]
print("Must be 1: number = ",solution(miLista))
"""


