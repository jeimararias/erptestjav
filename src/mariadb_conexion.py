import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='Arijei2023',
                db='pruebamdb'
            )
        except Error as ex:
            print ("Error al intentar la conexión: {0}".format(ex))

    def mostrarJobs(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("Select * from jobs order by Job_Id asc")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print ("Error al intentar la conexión: {0}".format(ex))

    def registrarJob(self, job):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="Insert into jobs (Job_Id, Job) Values ({0}, '{1}')"
                cursor.execute(sql.format(job[0],job[1]))
                self.conexion.commit()
                print ("¡ Job registrado !\n")
                return "OK"
            except Error as ex:
                print ("Error al intentar la conexión: {0}".format(ex))
                return "Error al intentar la conexión: {0}".format(ex)

    def actualizarJob(self, job):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="Update jobs set Job = '{0}' Where Job_Id = {1}"
                cursor.execute(sql.format(job[1],job[0]))
                self.conexion.commit()
                print ("¡ Job actualizado !\n")
                return "OK"
            except Error as ex:
                print ("Error al intentar la conexión: {0}".format(ex))
                return "Error al intentar la conexión: {0}".format(ex)

    def eliminarJob(self, codigoJob):
        #print("Tipo codigoJob: ", type(codigoJob))
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="Delete from jobs Where Job_Id = {0}"
                cursor.execute(sql.format(codigoJob))
                self.conexion.commit()
                print ("¡ Job {0} eliminado !\n".format(codigoJob))
                return "OK"
            except Error as ex:
                print ("Error al intentar la conexión: {0}".format(ex))
                return "Error al intentar la conexión: {0}".format(ex)
            finally:
                print("Continua...")

    def insertarVariosJobs(self):
        """
        data = [
        ('Jane', date(2005, 2, 12)),
        ('Joe', date(2006, 5, 23)),
        ('John', date(2010, 10, 3)),
        ]
        """        
        #print("Tipo codigoJob: ", type(codigoJob))
        if self.conexion.is_connected():
            misJobs=[ 
                      (30, "JOB 30"),
                      (31, "JOB 31"),
                      (32, "JOB 32"),
                      (33, "JOB 33")
                    ]
            try:
                cursor=self.conexion.cursor()
                #sql="Insert into jobs (Job_Id, Job) Values (?, ?)"  #Bajo otra medio
                sql="Insert into jobs (Job_Id, Job) Values (%s, %s)"
                cursor.executemany(sql, misJobs)        #Inserta varios registros
                self.conexion.commit()
                print ("¡ Job creados !\n")
                return "OK"
            except Error as ex:
                print ("Error al intentar la conexión: {0}".format(ex))
                return "Error al intentar la conexión: {0}".format(ex)
            finally:
                print("Continua...")
