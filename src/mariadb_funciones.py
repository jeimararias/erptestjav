
def listarJobs(jobs):
    print("\nJobs:\n")
    contador=1
    for cur in jobs:
        datos="{0}. Código: {1}  |  Nombre: {2}"
        print(datos.format(contador, cur[0], cur[1]))
        contador += 1
    print ("  ")

def pedirDatosRegistro():
    codigoCorrecto=False
    while (not codigoCorrecto):
        try:
            codigo=int(input("Ingrese código: "))
            if codigo < 1 or codigo > 300:
                raise ValueError("Numero debe estar entre 1 y 300")
            codigoCorrecto=True
        except Exception as ex:
            print("Codigo incorrecto..", ex)
    nombre=input("Ingrese nombre: ")

    job = (codigo, nombre)
    return job

def pedirDatosActualizacion(jobs):
    listarJobs(jobs)
    existeCodigo=False
    codigo=int(input("Ingrese código a actualizar: "))

    for job in jobs:
        if job[0] ==  codigo:
            existeCodigo=True
            break
    
    if existeCodigo:
        nombre=input("Ingrese nuevo nombre: ")
        job = (codigo, nombre)
    else:
        job = None

    return job

def pedirDatosEliminacion(jobs):
    listarJobs(jobs)
    existeCodigo=False
    codigo=int(input("Ingrese código a eliminar: "))

    for job in jobs:
        if job[0] ==  codigo:
            existeCodigo=True
            break
    
    if not existeCodigo:
        codigo = ""

    return codigo
