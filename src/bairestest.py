

def solution(queries):
    if len(queries) < 0 or len(queries) > 100:
        return ["Error tamaño de los queries debe estar entre 1 y 100"]

    containerresponse=[]
    containerint=[]
    for query in queries:
        #print(query[0], query[1])
        if query[0]=="ADD":
            isNumok=False
            if query[1].isnumeric() and float(query[1]) >= -100 and float(query[1])<=100:
                containerint.append(float(query[1]))
                containerresponse.append("")
            else:
                containerresponse.append("Error en numero: "+query[1])
        elif query[0]=="EXISTS":
            if float(query[1]) in (containerint):
                containerresponse.append("true")
            else:
                containerresponse.append("false")
        elif query[0]=="GET_NEXT":
            #print("Max value: ",max(containerint))
            valor=""
            for i in range(int(query[1]), int(max(containerint)+1)):
                #print("Paso: ",i)
                try:
                    x=containerint.index(i)
                    if int(containerint[x]) > int(query[1]):
                       valor=str(int(containerint[x]))
                       break
                    else:
                        pass
                except:
                    pass

            containerresponse.append(valor)

        elif query[0]=="REMOVE":
            try:
                containerint.remove(float(query[1]))
                containerresponse.append("true")
            except:
                containerresponse.append("false")
        else: 
            containerresponse.append("Opcion no disponible")

    return containerresponse

"""
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "2"],
    ["ADD", "3"],
    ["EXISTS", "1"],
    ["EXISTS", "2"],
    ["EXISTS", "3"],
    ["REMOVE", "2"],
    ["REMOVE", "1"],
    ["EXISTS", "2"],
    ["EXISTS", "1"]]
"""

"""    
queries=[["ADD","1"], 
 ["ADD","2"], 
 ["ADD","2"], 
 ["ADD","3"], 
 ["EXISTS","1"], 
 ["EXISTS","2"], 
 ["EXISTS","3"], 
 ["REMOVE","2"], 
 ["REMOVE","1"], 
 ["EXISTS","2"], 
 ["EXISTS","1"]]
"""
 
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "2"],
    ["ADD", "4"],
    ["GET_NEXT", "1"],
    ["GET_NEXT", "2"],
    ["GET_NEXT", "3"],
    ["GET_NEXT", "4"],
    ["REMOVE", "2"],
    ["GET_NEXT", "1"],
    ["GET_NEXT", "2"],
    ["GET_NEXT", "3"],
    ["GET_NEXT", "4"]
]

#print(queries)
print(solution(queries))

#the output should be solution(queries) = ["", "", "", "", "2", "4", "4", "", "true", "2", "4", "4", ""]




    
