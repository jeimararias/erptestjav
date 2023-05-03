# Archivo de configuraciones
import pyodbc

class DevelopmentConfig():
    DEBUG = True

config = {
    'development' : DevelopmentConfig
}

def connection():
    svr = 'JAVIATECH\SQLEXPRESS' #Your server name
    db = 'ERPTESTJAV' 
    usr = 'sa' #Your login
    pwd = 'Arijei2022' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+svr+';DATABASE='+db+';UID='+usr+';PWD='+ pwd
    conn = pyodbc.connect(cstr)
    return conn
