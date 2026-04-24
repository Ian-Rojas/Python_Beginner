# Ejemplo y uso de while
# cont = 1
# while cont<=3:
#     print(f"Contador {cont}")
#     cont+=1

# pin = 3535

# code=int(input("Ingrese su pin: "))

# while code!=pin:
#     print("Error, Intente otra vez")
#     code=int(input("Ingrese su pin: "))
# print("Pin Correcto!")

# Usando while, pida al usuario un número
# Y muestre su tabla de multiplicación hasta el 10
cont=1

num=int(input("Ingrese un número: "))

while cont <= 10:
    print(f"Tabla de el número: {cont}")
    print(f"La tabla de multiplicar es:", cont*num)
    cont+=1