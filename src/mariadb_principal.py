#----------Video ejemplo youtube: https://www.youtube.com/watch?v=d3mYv1r4DkQ -----#

from mariadb_conexion import DAO
import mariadb_funciones as funciones

def menuPrincipal():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        print("--- Menú principal---")
        print("1.- Listar Jobs")
        print("2.- Add Jobs")
        print("3.- Upd Jobs")
        print("4.- Del Jobs")
        print("5.- Salir")
        print("6.- Insertar varios")
        print("7.- Insertar One con fecha Lista")
        print("8.- Insertar One con fecha Dictionario")
        print("9.- Pendiente")
        print("------")
        opcion=int(input("Digite opcion: "))

        if opcion<1 or opcion>9:
            print("Opcion incorrecta ingrese nuevamente")
        elif opcion==5:
            continuar=False
            print("Gracias por usar el sistema")
            break
        else:
            opcionCorrecta=True
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    #print(opcion)
    dao = DAO()

    if opcion == 1:
        try:
            jobs=dao.mostrarJobs()
            if len(jobs)>0:
                funciones.listarJobs(jobs)
            else:
                print("No se encontraron trabajos..")
        except:
            print("Ocurrió un error en lectura..")
        finally:
            print("Finalizando...")
    elif opcion == 2:
        job = funciones.pedirDatosRegistro()
        try:
            dao.registrarJob(job)
        except:
            print("Ocurrió un error ..")
    elif opcion == 3:
        try:
            jobs = dao.mostrarJobs()
            if len(jobs) > 0:
                job = funciones.pedirDatosActualizacion(jobs)
                if job:
                    dao.actualizarJob(job)
                else:
                    print("Código de Job a actualizar no encontrado..\n")
            else:
                print("No se encontraron Jobs...")               
        #except:
        finally:
            print("Ocurrió un error ..")
    elif opcion == 4:
        try:
            jobs = dao.mostrarJobs()
            if len(jobs) > 0:
                codigoEliminar=funciones.pedirDatosEliminacion(jobs)
                if not(codigoEliminar == ""):
                    dao.eliminarJob(codigoEliminar)
                else:
                    print("Código de Job no encontrado\n")
            else:
                print("No se encontraron Jobs...")
        except:
            print("Ocurrió un error ..")
    elif opcion == 6:
        try:
            dao.insertarVariosJobs()
        except:
            print("Ocurrió un error ..")
    elif opcion == 7:
        try:
            dao.insertarOneJob_Lista()
        except:
            print("Ocurrió un error ..")
    elif opcion == 8:
        try:
            dao.insertarOneJob_Dict()
        #except:
            #print("Ocurrió un error ..")
        finally:
            pass
    else:
        print("Opcion no valida")

if __name__ == '__main__':  ##Ingreso a la función principal
    menuPrincipal()

