"""
  Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13.
"""

# Declaración de constantes
EXPHOURS = 1500
CHEHOURS = 1300
MINHOURS = 1100
EXPBONUS = 18
CHEBONUS = 15
MINBONUS = 13


workedHours = int(
    input('Ingrese la cantidad horas trabajadas por el empleado: '))

# Verifica si las horas trabajadas son menores a 193
if (0 < workedHours < 193):
  # Verifica rango de horas/pagos corresponde las horas trabajadas.
    if (workedHours > 120):
        grossSalary = workedHours * EXPHOURS
        bonusAmount = EXPBONUS * grossSalary / 100
    elif (80 <= workedHours <= 120):
        grossSalary = workedHours * CHEHOURS
        bonusAmount = CHEBONUS * grossSalary / 100
    else:
        grossSalary = workedHours * MINHOURS
        bonusAmount = MINBONUS * grossSalary / 100

    # Muestra por pantalla los resultados.
    print(
        f'El sueldo bruto del empleado es: {grossSalary}, siendo {workedHours} las horas trabajadas.\n El total a cobrar es {grossSalary + bonusAmount}.')

else:
    print(f'Usted es un explotador laboral o un tonto, haga sus propios cáculos.')
