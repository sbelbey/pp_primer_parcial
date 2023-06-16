"""
Escribe un programa que calcule el promedio final de una materia, 
basado en 3 notas de parciales, indicando por pantalla si el alumno aprobó o debe recursar la materia 
(se aprueba con 6).
"""

nota1 = float(input('Ingrese la primera nota: '))
nota2 = float(input('Ingrese la segunda nota: '))
nota3 = float(input('Ingrese la tercera nota: '))

# Calcula el promedio de las tres notas ingresadas y lo guarda en la variable
promedio = (nota1 + nota2 + nota3) / 3


# Verifica si el promedio es mayor o igual a 6
if (promedio >= 6):
    print('Usted ha aprobado la materia.', promedio, 'es su promedio', sep=" ")
else:
    print('Usted debe cursar.', promedio, 'es su promedio', sep=" ")
