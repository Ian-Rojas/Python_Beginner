# Explicación y uso de match
total=0
op=0
while op != 4:
    print("1.- PC Ryzen $800.000")
    print("2.- LGTV 55 Pulgadas $450.000")
    print("3.- Parlante JBL Pure Sound $90.000")
    print("4.- Salir")
    print("Selecciones una opcion: ")
    op=int(input())
    match op:
        case 1:
            print("Tiene que pagar:")
            total+=800000*1.19
        case 2:
            print("Tiene que pagar:")
            total+=450000*1.19
        case 3:
            print("Tiene que pagar:")
            total+=90000*1.19
        case 4:
            print("Saliendo...")
            print(f"El total a pagar con IVA es: {total}")
        case _:
            print("Opción Inválida")