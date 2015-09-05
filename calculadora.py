__author__ = 'francesc'


def convertString(str):
    try:
        returnValue = int(str)
    except ValueError:
        returnValue = float(str)
    return returnValue


def addition(a, B):
    return convertString(a) + convertString(B)


def subtraction(a, B):
    return convertString(a) - convertString(B)


def multiplication(a, B):
    return convertString(a) * convertString(B)


def division(a, B):
    return convertString(a) / convertString(B)

keepProgramRunning = True

print ("Calculadora")

while keepProgramRunning:
    print ("Que te gustaria hacer?")

    print ("0: Sumar")
    print ("1: Restar")
    print ("2: Multiplicar")
    print ("3: Dividir")
    print ("4: Salir")

    # Capture the menu choice.
    choice = raw_input()

    if choice == "0":
        numberA = raw_input("Introduce tu primer numero: ")
        numberB = raw_input("Introduce el segundo numero: ")
        print ("El resultado es:")
        print addition (numberA, numberB)
    elif choice == "1":
        numberA = raw_input("Introduce tu primer numero:  ")
        numberB = raw_input("Introduce el segundo numero: ")
        print "El resultado es:"
        print subtraction(numberA, numberB)
    elif choice == "2":
        numberA = raw_input("Introduce tu primer numero: ")
        numberB = raw_input(": ")
        print ("El resultado es:")
        print multiplication(numberA, numberB)
    elif choice == "3":
        numberA = raw_input("Introduce tu primer numero: ")
        numberB = raw_input("Introduce el segundo numero: ")
        print ("El resultado es:")
        print division(numberA, numberB)
    elif choice == "4":
        print ("Hasta luego Lucas !!!")
        keepProgramRunning = False
    else:
        print ("Por Favor, introduce una opcion correcta.")
        print "\n"