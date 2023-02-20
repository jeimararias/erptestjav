from flask import Flask, jsonify
from config import config
from fastavro import writer, reader, parse_schema
import pyodbc  ## from flask_mysqldb import MySQL
import pandas

def connection():
    svr = 'JEIMARARIAS\SQLEXPRESS' #Your server name 
    db = 'ERPTESTJAV' 
    usr = 'sa' #Your login
    pwd = 'Arijei2022' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+svr+';DATABASE='+db+';UID='+usr+';PWD='+ pwd
    conn = pyodbc.connect(cstr)
    return conn

# Crear un servidor
app=Flask(__name__)
#conn = connection()

# Loads from csv files
@app.route('/erpjav/<tablename>/<nrows>', methods=['POST'])
def load_table(tablename, nrows):
    nrows = int(nrows)
    if nrows<1:
        nrows=500
    elif nrows>1000:
        nrows=1000

    if tablename=="departments":
        filename = 'files\departments.csv'
        sql="Insert into dbo.Departments (Id, Department) Values (?, ?);"
    elif tablename=="jobs":
        filename = 'files\jobs.csv'
        sql="Insert into dbo.Jobs (Id, Job) Values (?, ?);"
    elif tablename=="hired_employees":
        filename = 'files\hired_employees.csv'
        sql="Insert into dbo.HiredEmployees (Id, Name, Datetime_Hired, Department_Id, Job_Id) Values (?, ?, ?, ?, ?);"
    else:
        return jsonify({'Message':"Error in file name to read"})

    ## Ejecución del proceso ##
    conn = connection()
    cursor = conn.cursor()
    df = pandas.read_csv(filename, sep=',', header=None, chunksize=nrows)   #header=0
    log_errados = []    
    for data in df:
        batch=data.values.tolist()
        for row in batch:
            try:
                # Validations
                #for col in row:
                #    print(col)
                #    if col == None:
                #        print("registro errado \n")
                cursor.execute(sql, row)    #Inserta el registro
            except Exception as ex:
                log_errados.append(row)     #print(row)
            finally:
                cursor.commit()  ##Toca hacer el commit inmediatamente porque sino, se pierden registros ***
 
        #cursor.executemany(sql, batch) #Inserta el lote

    #Guarda log de errores
    df = pandas.DataFrame(log_errados) #, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
    df.to_csv(filename + '.log', header=None, index=None)

    ##Cierres de cursor y conexion
    cursor.close()
    conn.close()

    return jsonify({'Message': tablename + " file was loaded. See errors in " + filename + ".log"})

#Backup por tabla en formato avro
@app.route('/erpjav1/backup/<tablename>', methods=['GET'])
def backup_avro(tablename):
    if tablename=="departments":
        filename = 'backups\departments.avro'
        sql="SELECT * FROM dbo.Departments order by Id;"
    elif tablename=="jobs":
        filename = 'backups\jobs.avro'
        sql="SELECT * FROM dbo.Jobs order by Id;"
    elif tablename=="hired_employees":
        filename = 'backups\hired_employees.avro'
        #sql="SELECT * FROM dbo.HiredEmployees order by Id;"
        sql="SELECT Id, [Name], Replace(convert(varchar,Datetime_Hired,111),'/','-')+'T'+convert(varchar,Datetime_Hired, 108)+'Z' Datetime_Hired, Department_Id, Job_Id FROM dbo.HiredEmployees order by Id;"
    else:
        return jsonify({'Message':"Error in table name to backup"})

    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        # Generate dictionaries
        Table_avro=[]
        for row in data:
            if tablename=="departments":
                r_avro={'Id':row[0], 'Department':row[1]}
            elif tablename=="jobs":
                r_avro={'Id':row[0], 'Job':row[1]}
            elif tablename=="hired_employees":
                r_avro={'Id':row[0], 'Name':row[1], 'Datetime_Hired':row[2], 'Department_Id':row[3], 'Job_Id':row[4]}
            Table_avro.append(r_avro)
            #print(r_avro)

        # Use schema
        file_schema = data_schema(tablename)
        parsed_schema = parse_schema(file_schema)

        # Convert pandas.DataFrame to records - list of dictionaries
        # records = data.to_dict('records') # Esta sentencia convierte df pandas.

        # Write to Avro file
        with open(filename, 'wb') as out:
            writer(out, parsed_schema, Table_avro)

        return jsonify({'Message':"Table "+tablename+' has backed up in avro format: OK'})
    
    except Exception as ex:
        return jsonify({'Message':"Error: I couldn't backup table "+tablename})
    finally:
        conn.close()

#restore por tabla desde backup en formato avro
@app.route('/erpjav1/restore/<tablename>', methods=['PUT'])
def restore_avro(tablename):
    if tablename=="departments":
        filename = 'backups\departments.avro'
        sql="Insert into dbo.Departments (Id, Department) Values (?, ?);"
    elif tablename=="jobs":
        filename = 'backups\jobs.avro'
        sql="Insert into dbo.Jobs (Id, Job) Values (?, ?);"
    elif tablename=="hired_employees":
        filename = 'backups\hired_employees.avro'
        sql="Insert into dbo.HiredEmployees (Id, Name, Datetime_Hired, Department_Id, Job_Id) Values (?, ?, ?, ?, ?);"
    else:
        return jsonify({'Message':"Error in table name to backup"})

    try:
        avro_records = []       # 1. List to store the records
        # 2. Read the Avro file
        with open(filename, 'rb') as fo:
            avro_reader = reader(fo)
            for record in avro_reader:
                avro_records.append(record)

        df_avro = pandas.DataFrame(avro_records)  # Convert to dataframe pandas

        conn = connection()
        cursor = conn.cursor()
        batch=df_avro.values.tolist()
        for row in batch:
            print(row)
            #try:
            cursor.execute(sql, row)    #Inserta el registro
            #except Exception as ex:
                #log_errados.append(row)     #print(row)
            cursor.commit()  ##Toca hacer el commit inmediatamente porque sino, se pierden registros ***

        cursor.close()
        return jsonify({'Message':"Table "+tablename+' has been retored from avro format: OK'})
    
    #except Exception as ex:
        #return jsonify({'Message':"Error: I couldn't restore table "+tablename})
    finally:
        conn.close()

# Return a schema for each table of the parameter
def data_schema(filename):
    schema = {}
    if filename == 'jobs':
        schema = {
            'doc': 'Jobs name',
            'name': 'Jobs',
            'namespace': 'erp_jav',
            'type': 'record',
            'fields': [
                {'name': 'Id', 'type': 'int'},
                {'name': 'Job', 'type': 'string'}
            ]
        }    
    elif filename == 'departments':
        schema = {
            'doc': 'Departments name',
            'name': 'Departments',
            'namespace': 'erp_jav',
            'type': 'record',
            'fields': [
                {'name': 'Id', 'type': 'int'},
                {'name': 'Department', 'type': 'string'}
            ]
        }
    elif filename == 'hired_employees':
        schema = {
            'doc': 'Hired employees name',
            'name': 'HiredEmployees',
            'namespace': 'erp_jav',
            'type': 'record',
            'fields': [
                {'name': 'Id', 'type': 'int'},
                {'name': 'Name', 'type': 'string'},
                {'name': 'Datetime_Hired', 'type': 'string'},                
                #{'name': 'Datetime_Hired', 'type': {'type': 'string', 'logicalType': 'time-millis'}},     ##genera error time encode           
                {'name': 'Department_Id', 'type': 'int'},
                {'name': 'Job_Id', 'type': 'int'}
            ]
        }
    return schema

@app.route('/erpjav/<report_name>', methods=['GET'])
def gen_reports(report_name):  # antes listar_cursos
    try:
        if report_name=="employees_quarters":
            sql="Select * from dbo.vwEmployeesHiredByQuarter where Year_Hired = 2021 Order by Year_Hired, Department, Job;"
            report_title="Employees hires by Department/Job in year 2021"
        elif report_name=="employees_average":
            sql="Select * from dbo.vwEmployeesHiredByDeparments_Year where Year_Hired = 2021 and TotHiresXDep_Year >	AvgYear Order by Year_Hired, TotHiresXDep_Year desc;"
            report_title="Total Employees hires in year 2021 greater than average company"
        else:
            return jsonify({'Message':"** Error in report name entered **"})

        conn = connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()

        # mapping records: Convert data framework to list
        resume_result=[]
        for row in data:
            if report_name=="employees_quarters":
                row_result={'Year_Hired':row[0], 'Department':row[1], 'Job':row[2], 'Q1':row[3], 'Q2':row[4], 'Q3':row[5], 'Q4':row[6]}
            elif report_name=="employees_average":
                row_result={'Year_Hired':row[0], 'Department_Id':row[1], 'Department':row[2], 'TotHiresXDep_Year':row[3], 'AvgYear':row[4]}
            resume_result.append(row_result)
        return jsonify({'Result':resume_result, 'Message':report_title})    
    except Exception as ex:
        return jsonify({'Message':"Error !!!"})
    finally:
        conn.close()

# Genera el contenido de una tabla en Json
@app.route('/erpjav', methods=['GET'])
def index_erp():  # antes listar_cursos
    conn = connection()
    try:
        cursor = conn.cursor()
        sql="SELECT * FROM dbo.Departments order by Id"
        cursor.execute(sql)
        #for row in cursor.fetchall():
        #    cars.append({"id": row[0], "name": row[1], "year": row[2], "price": row[3]})
        data=cursor.fetchall()
        # mapping records
        Deparments=[]
        for row in data:
            department={'Id':row[0], 'Department':row[1]}
            Deparments.append(department)

        #print(data)
        #return "Hi Jeimar !! You app is going conectar sql .."
        return jsonify({'Deparments':Deparments, 'Message':"Department list"})    
    except Exception as ex:
        #return "Error"
        return jsonify({'Message':"Error !!!"})
    finally:
        conn.close()

def pagina_no_encontrada(error):
    return "<h1>Página no existe...</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()   #app.run(debug=True)
