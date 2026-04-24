def calculadora():
    op=0
    def suma():
        num1=int(input("Seleccione un número: "))
        num2=int(input("Seleccione otro número: "))
        print(f"La suma de los números es: {num1+num2}")
    def resta():
        num1=int(input("Seleccione un número: "))
        num2=int(input("Seleccione otro número: "))
        print(f"La resta de los números es: {num1-num2}")
    def multi():
        num1=int(input("Seleccione un número: "))
        num2=int(input("Seleccione otro número: "))
        print(f"La multiplicación de los números es: {num1*num2}")
    def divi():
        num1=int(input("Seleccione un número: "))
        num2=int(input("Seleccione otro número: "))
        print(f"La division de los números es: {num1/num2}")
    while op != 5:
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- Division")
        print("5.- Salir")
        print("Seleccione una opción: ")
        op=int(input())
        match op:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multi()
            case 4:
                divi()
            case 5:
                print("Saliendo...")
            case _:
                print("Opción Inválida")
calculadora()