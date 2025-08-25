def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

def calculadora():
    print("Calculadora básica en Python")
    print("Operaciones disponibles: suma, resta, multiplicación, división")

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    operacion = input("Escribe la operación: ").lower()

    if operacion == "suma":
        print("Resultado:", suma(a, b))
    elif operacion == "resta":
        print("Resultado:", resta(a, b))
    elif operacion == "multiplicación" or operacion == "multiplicacion":
        print("Resultado:", multiplicacion(a, b))
    elif operacion == "división" or operacion == "division":
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida")

calculadora()
