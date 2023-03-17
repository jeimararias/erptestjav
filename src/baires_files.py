#from io import *
import io
import os

"""
f=open("archivo.txt","w")
data="Estupendo dia para estudiar python \n hoy viernes y también miércoles"
f.write(data)
f.close()

f=open("archivo.txt","a")
data="\nsiempre es una buena opcion para estudia python"
#f.write(data)
f.close()

f=open("archivo.txt","r")
data=f.readlines()

print("type of data: ",type(data),"\n",data)
f.seek(0)
print("Nueva lectura: \n",f.read())

f.close()
"""
def getFileSize(data):
   cols=data[0].split("|")
   #print("Columnas leidas: ", cols)
   return int(cols[2])

def solutions(queries):
    listReturn=[]
    for q in queries:
        if q[0] == "ADD_FILE":
            try:
              f=open(q[1],"r")
              data=f.readlines()
              size=getFileSize(data)
              #print("Tipo data:", type(data), "  size= ", size)
              if size < int(q[2]):
                 listReturn.append(q[0]+":File exists: Less size")
              else:
                 listReturn.append(q[0]+":File exists: GTE size")
            except FileNotFoundError as ex:
              #print(ex)
              f=open(q[1],"w")
              f.writelines(q[0]+"|"+q[1]+"|"+q[2])
              listReturn.append(q[0]+":true")
            finally:
              f.close()
        elif q[0] == "GET_FILE_SIZE":
            try:
              f=open(q[1],"r")
              data=f.readlines()
              size=getFileSize(data)
              #print("Tipo data:", type(data), "  size= ", size)
              listReturn.append(q[0]+":"+str(size))
            except FileNotFoundError as ex:
              listReturn.append(q[0]+":File doesn't exist")
            finally:
              f.close()
        elif q[0] == "DELETE_FILE":
          file_path=str(q[1])
          #print(file_path)
          if os.path.isfile(file_path):
            #print("File exists...")
            os.remove(file_path)
            listReturn.append(q[0]+":true")
          else:
            #print("FILE NOT EXISTS...")
            listReturn.append(q[0]+":File doesn't exist")
        else:
            listReturn.append(q[0]+":Option not allowed")
    return listReturn  

#"""
queries = [
  ["ADD_FILE", "./files/file.txt", "10"],
  ["ADD_FILE", "./files/file.txt", "5"],
  ["GET_FILE_SIZE", "./files/file.txt"],
  ["DELETE_FILE", "./non-existing.file"],
  ["DELETE_FILE", "./files/file.txt"],
  ["GET_FILE_SIZE", "./not-existing.file"]
]
#"""

"""
queries = [
  ["ADD_FILE", "\\dir1\\dir2\\file.txt", "10"],
  ["ADD_FILE", "\\dir1\\dir2\\file.txt", "5"],
  ["GET_FILE_SIZE", "\\dir1\\dir2\\file.txt"],
  ["DELETE_FILE", "\\non-existing.file"],
  ["DELETE_FILE", "\\dir1/dir2/file.txt"],
  ["GET_FILE_SIZE", "\\not-existing.file"]
]
"""

resultados=solutions(queries)
print(resultados)
