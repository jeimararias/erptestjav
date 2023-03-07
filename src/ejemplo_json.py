#from flask import jsonify
import json
import pandas
from config import connection

#Open json file
def open_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def load_table_json(tablename, data):
    if tablename=="departments":
        sql="Insert into dbo.Departments (Id, Department) Values (?, ?);"
    elif tablename=="jobs":
        sql="Insert into dbo.Jobs (Id, Job) Values (?, ?);"
    elif tablename=="hired_employees":
        sql="Insert into dbo.HiredEmployees (Id, Name, Datetime_Hired, Department_Id, Job_Id) Values (?, ?, ?, ?, ?);"
    else:
        print("Error en nombre de tabla...")

    ## Ejecución del proceso ##
    conn = connection()
    cursor = conn.cursor()
    log_errados = []    
    for row in data:
        #print ("Tipo row:", type(row), "   Data_row: ", row["Id"], " | ", row["Department"])
        reg=[row["Id"],row["Department"]]
        try:
            # Validations
            #for col in row:
            #    print(col)
            #    if col == None:
            #        print("registro errado \n")
            #print("Tipo reg: ",type(reg), "reg: ", reg)
            cursor.execute(sql, reg)    #Inserta el registro
            #cursor.executemany(sql, batch) #Inserta el lote
        except Exception as ex:
            log_errados.append(row)     #print(row)
        finally:
            cursor.commit()  ##Toca hacer el commit inmediatamente porque sino, se pierden registros ***

    cursor.close()
    conn.close()

    #Guarda log de errores
    df = pandas.DataFrame(log_errados) #, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
    df.to_csv('files\\' + tablename + '.log', header=None, index=None)

    return True

def save_table_json(tablename):
    sql="""Select Id,	[Name],	Replace(convert(varchar,Datetime_Hired,111),'/','-')+'T'+convert(varchar,Datetime_Hired, 108)+'Z' Datetime_Hired, 
       Year_Hired,	Quarter_Hired,	Department_Id,	Department,	Job_Id,	Job from """ + tablename + ";"
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    print("Type of data: ",type(data))
    print(data)

    data_dict = []      #Lista
    for row in data:
        row_json = {"Id":row[0], "Name":row[1], "Datetime_Hired":row[2], "Year_Hired":row[3], "Quarter":row[4], "Department_Id":row[5], "Department":row[6], "Job_Id":row[7], "Job":row[8]}
        data_dict.append(row_json)

    print("Dict: \n",data_dict)
    with open('files\\' + tablename + '.json', 'w') as json_file:
        json.dump(data_dict, json_file) #json_file es una lista de diccionarios
        #json.dump(jsonify(data_dict), json_file) #json_file es una lista de diccionarios

    cursor.close()
    conn.close()

#data=open_json("files\departments.json")
#load_table_json("departments", data)

save_table_json("vwEmployees")

