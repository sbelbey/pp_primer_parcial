"""
Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, 
basado en el año de nacimiento.
"""

import datetime  # Importa el módulo datetime para trabajar con fechas y tiempos


# Obtiene el año actual utilizando el objeto datetime y lo guarda en la variable current_year
current_year = datetime.datetime.now().year
year_birth = int(input('Ingrese el año de nacimiento de la persona: '))

print(
    f'La persona debería cumplir o cumplió este año: {current_year - year_birth}')
