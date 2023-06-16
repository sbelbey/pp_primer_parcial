"""
Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de
personas ingresada por el usuario.
"""

# Inicializando el contador.
count = 0

usrRequire = int(input(
    f"Ingrese la cantidad de alumnos que quiere ingresar el nombre, el apellido y la edad: "))

"""
  Comprueba que la cantidad de personas ingresadas no sean más que las ingresadas por el usuario 
  y repite la operación dicha cantidad de veces.
"""
while count < usrRequire:
  # Solicitud de los datos
    name = input(f"Ingrese el nombre del estudiante Nº {count+1}: ")
    last_name = input(f"Ingrese el apellido del estudiante Nº {count+1}: ")
    age = input(f"Ingrese la edad del estudiante Nº {count+1}: ")
    print(
        f"El nombre completo del estudiante Nº {count+1} es {name} {last_name} y su edad es {age}")

  # Evita un bucle infinito
    count += 1

print("Fin del programa.")
