class FancyTuple:
    # Implement the FancyTuple here

    def __init__(self, *t):
        self.first = None
        self.second = None
        self.third = None
        self.fourth = None
        self.fifth = None
        for l in (0, len(t)-1):
            if l==0:
                self.first = t[0]
            elif l==1:
                self.second = t[1]
            elif l==2:
                self.third = t[2]
            elif l==3:
                self.fourth = t[3]
            elif l==4:
                self.fifth = t[4]
            else:
                break
        
        self.value = str(len(t))
        #return None #str(len(l)) #self.value
    
    def __str__(self):
        #Como el constructor devuelve un None, es necesaria esta Función adicional 
        #que para retornar un valor string diferente en el constructor
        #** Debe ser string ***
        return self.value

x=FancyTuple("Dog","Cat","Fish").third
print(x)

#Devolver otro valor
y=FancyTuple("Dog","Cat","Fish")
print("Return value. Longitud entrada: ", y)



"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = [input() for _ in range(n)]

    t = FancyTuple(*items)

    q = int(input())
    for _ in range(q):
        command = input()
        if command == "len":
            fptr.write(str(len(t)) + "\n")
        else:
            try:
                elem = getattr(t, command)
            except AttributeError:
                fptr.write("AttributeError\n")
            else:
                fptr.write(elem + "\n")
    fptr.close()
"""
