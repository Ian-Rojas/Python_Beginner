autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}

def mostrarAutos(diccio):
    for id, auto in diccio.items():
        print(f"{id}: {auto}")

def mostrarAutosVendidos(diccio):
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            print(f"{id}: {auto}")

def autos_vendidos_por_marca(diccio,marca):
    total=0
    for id, auto in diccio.items():
        if operaciones[id][1]!="Pendiente":
            if auto[0].lower()==marca.lower():
                total+=1
    print(f"El total de autos vendidos es {total} en la marca {marca}")

def actualizarEstado(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][1]=nueva_fecha
        return True
    else:
        return False
# while True:
#     id = input("Ingrese un id del auto: ")
#     fecha = input("Ingrese la fecha de venta: ")
#     if actualizarEstado(id, fecha):
#         print("Exito, nueva fecha de venta actualizada.")
#     else:
#         print("Metió la pata")
#     next=input("Desea actualizar otro vehiculo (s/n)?: ")
#     if next.lower()!= "s":
#         break

# Establecer fecha de venta por pendiente


def validarString(id_auto):
    if id_auto != "" and id_auto != " ":
        return True
    else:
        return False
    
def validarAnio(f):
    if f<1900:
        return True
    else:
        return False

def validarRanking(r):
    if r>=1 and r<=5:
        return True
    else:
        return False


def creAuto():
    id=input("Ingresa el nuevo ID: ")
    if validarString(id):
        print("Dato Inválido")
        return
    marca=input("Ingresa el marca: ")
    if validarString(marca):
        print("Dato Inválido")
        return
    modelo=input("Ingresa el nuevo modelo: ")
    if validarString(modelo):
        print("Dato Inválido")
        return
    anio=int(input("Ingresa el año: "))
    if validarAnio(anio):
        print("El año debe ser mayor a 1900.")
        return
    ranking=int(input("Ingresa el ranking: "))
    if validarRanking(ranking):
        print("El ranking debe ser entre 1 y 5.")
        return
    fecha=input("Ingrese la fecha (dd-mm-yyyy): ")
    if validarString(fecha):
        print("Dato Inválido")
        return
    autos[id]={marca, modelo,anio,ranking}
    operaciones[id]={fecha, 'Pendiente'}

def eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
        

# Tarea Hacer un menú con todas las funciones que
# Hicimos en clase, debe tener try - except