"""
Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. 
El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).
"""

exchange = int(
    input(
        "Ingrese el numero de la opción según corresponda: \n1. Cambiar de pesos a dolares. \n2.Cambiar de dolares a pesos.\n"
    )
)

# Verifica si la opción ingresada no es igual a 1 ni igual a 2
if (exchange != 1) or (exchange != 2):
  # Verifica cual es la opción ingresada
    if (exchange == 1):
        pesos = int(
            input("Ingrese la cantidad de pesos que desea convertir a dólares: "))
        dolar = int(input("Ingrese el valor de un dolar en pesos: "))
        print("La cantidad de dólares que puede comprar con sus pesos es: ", pesos/dolar)
    else:
        dolares = int(
            input("Ingrese la cantidad de dolares que desea convertir a pesos: "))
        dolar = int(input("Ingrese el valor de un dolar en pesos: "))
        print("La cantidad de dólares que puede comprar con sus pesos es: ", dolares*dolar)
else:
    print("Ingresó una opción incorrecta")
