import sys
import re

#print (5//2)
#a={1:9, 2:8}
#print(a.get(3))


#print(a.items())

#a = 7
#print(a.__str__())

#print(set([1,2,1]) == set([1,2]))

#print("Hello"'word '*2)

#print(sys.path)

"""
def listSkills(val, list[]):
    list.append(val)
    return list

list1=listSkills("NodeJS")
list2=listSkills("Java", [])
list3=listSkills("ReactJS")

print("%s" % list1)
print("%s" % list2)
print("%s" % list3)
"""

#numbers = [10, 15, 21, 33, 42, 55]

a = [1,2,3,4]
b = [sum(a[0:x+1]) for x in range(0,len(a))]
print("lista sum: ", b)

print(2**(3**2), (2**3)**2, (2**3)**3)

base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))
print("Map Resultado: ",numbers_powers)

mapped_numbers = list(map(lambda x: x ** 2, powers))

print("Map quadrado: ",mapped_numbers)


l = [1,2,3,4,5]
m = map(lambda x: 2**x, l)
print("2**x:", list(m))


a = ["Welcome", "To", "Turing"]
print("-".join(a))

r = a

print(r)

#print(list(map(len(r), r)))
print("Tamaños:",list(map(len, r)))

#print(list(map(lambda r: len(r), r)))



# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Jéimar')
greet_user('Zulma')

# Lambda fucntion
#nombre_Funcion = lambda argument(s) : expression 
#lambda argument(s) : expression 

# Lambda function 
multiplica = lambda a, b : a * b

print("Multiplica: ", multiplica(2,3))

###########################

def assign_to_tank(aquarium_creatures, new_tank_number):
	def apply(x):
		x["tank number"] = new_tank_number
		return x
	return map(apply, aquarium_creatures)

aquarium_creatures = [
	{"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
	{"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
	{"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
	{"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
	{"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
	{"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]

assigned_tanks = assign_to_tank(aquarium_creatures, 42)
print("New list: \n", list(assigned_tanks))

###--------------------Regular Expresion------------------------------###
print("Expresiones regulares: \n")
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group(0))

print(re.match("c", "abcdef"))    # No match
print(re.search("^c", "abcdef"))  # No match
print(re.search("^a", "abcdef"))  # Match

if re.match("c", "abcdef") == None:
	print("Esto es None: No encontrado")

print(re.fullmatch("p.*n", "python")) # Match
print(re.fullmatch("r.*n", "python")) # No match

print(re.match("X", "A\nB\nX", re.MULTILINE))  # No match
print(re.search("^X", "A\nB\nX", re.MULTILINE))  # Match
print(re.search("^X", "A\nBX", re.MULTILINE))  # No Match


frase = "Cython no es ningún lenguaje de programación y Nython tampoco pero Python sí"
patron = '^.ython'
palabras = re.findall(patron, frase)
print(palabras)

patron = '\\s.ython'
palabras = re.findall(patron, frase)
print(palabras)

frase = "Ramón y Román programan en Python"
patron = '.+n'
print(re.findall(patron, frase))
patron = '.+?n'
print(re.findall(patron, frase))

frase = "¡Esto es una frase! Además contiene signos de puntuación. ¿Los eliminamos?"
patron = '[^¡!.¿? ]+'
print(re.findall(patron, frase))

frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+'
print(re.findall(patron, frase))

frase = "Tengo dos correos electrónicos que son nombre.apellido@dominio.tld y nombre@dominio.com"
patron = '@([^ ]*)'
print(re.findall(patron, frase))

print(re.match(r"\W(.)\1\W", " ff "))
print(re.match("\\W(.)\\1\\W", " ff "))

frase = "Esto;es;una;lista"
list1 = frase.split(";")
print(list1)

print(list1[0:3])

"""
for i in range(10):
	print("i=",i) #,"  j=",j)

def wl(i)
	i = i + ', abc'return i

x=wl("xyz")
print(x)
"""

print([i.lower() for i in "TURING"])























