"""
  Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas.
"""

# Inicializando el contador.
count = 0

#Comprueba que la cantidad de personas ingresadas no sean más de 5 y repite la operación dicha cantidad de veces.
while count < 5:
  # Solicitud de los datos
    name = input(f"Ingrese el nombre del estudiante Nº {count+1}: ")
    last_name = input(f"Ingrese el apellido del estudiante Nº {count+1}: ")
    age = input(f"Ingrese la edad del estudiante Nº {count+1}: ")
    print(
        f"El nombre completo del estudiante Nº {count+1} es {name} {last_name} y su edad es {age}")

  #Evita un bucle infinito
    count += 1

print("Fin del programa.")
