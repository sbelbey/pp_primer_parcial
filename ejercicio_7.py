"""
Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas, 
escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual
a descontarse y las horas trabajadas en todo el año.
"""

# Declaración de constantes
EXPHOURS = 1500
CHEHOURS = 1300
MINHOURS = 1100
EXPBONUS = 18
CHEBONUS = 15
MINBONUS = 13
SUPERDISC = 5
MAXDISC = 3
MINDISC = 1


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

    # Calcula los descuentos según el salario anualizado.
    if (grossSalary * 12 > 2000000):
        discount = SUPERDISC * grossSalary / 100
    elif (1000000 <= grossSalary * 12 <= 2000000):
        discount = MAXDISC * grossSalary / 100
    else:
        discount = MINDISC * grossSalary / 100

    print(
        f'El sueldo bruto anual del empleado es: {grossSalary*12}, siendo {workedHours*12} las horas totales trabajadas.\n Su descuentos anuales son de {discount * 12}. \n Su bonificación anual es {bonusAmount * 12}, y el total a cobrar es {grossSalary * 12 - discount * 12 + bonusAmount * 12}.')

else:
    print(f'Usted es un explotador laboral, haga sus propios cáculos.')
