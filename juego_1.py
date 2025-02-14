import random

# input

print("--------------------------------")
n = int(input("Ingrese un numero entre (1-100): "))
print("--------------------------------")

# processing 

maq = random.randint(1,100)

i = 1

while n != maq:
    if n < maq:
        print("--------------------------------")
        print("El valor es mayor al elegido")
        print("--------------------------------")
    else:
        print("--------------------------------")
        print("El valor es menor al elegido")
        print("--------------------------------")

    print("--------------------------------")
    n = int(input("Ingrese un nùmero entre (1-100): "))
    print("--------------------------------")