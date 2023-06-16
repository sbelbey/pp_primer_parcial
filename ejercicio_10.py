"""
Escribe un programa que calcule el promedio general de una clase.
"""

# Inicializando el contador.
count = 0
accu = 0

usrRequire = int(input(
    f"Ingrese la cantidad de alumnos que quiere ingresar la nota: "))

while count < usrRequire:
  # Solicitud de los datos
    accu += int(input(f"Ingrese la nota del almuno Nº {count + 1}: "))
  # Evita un bucle infinito
    count += 1

# Calcula y muestra por pantalla lo solicitado
print(f"El promedio general de la clase es {accu/usrRequire}")
