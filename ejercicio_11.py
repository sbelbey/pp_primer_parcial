"""
Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si es número es par o impar.
b. Cuanto es la suma total de todos los números mostrados.
c. Cuanto es la suma total de todos los números pares mostrados.
d. Cuanto es la suma total de todos los números impares mostrados.
"""

count = 0
oddAccum = 0
genAccum = 0
evenAccum = 0

while count < 10:
    count += 1
    # Comprueba si el nume es par o no.
    if count % 2 == 0:
        print(f"El número par es: {count}")
        oddAccum += count
        genAccum += count
        # Vuelva a iniciar el bucle
        continue

    print(f"El número impar es: {count}")
    evenAccum += count
    genAccum += count

print(
    f"La suma de todos los números es: {genAccum}, la suma de todos los números impares es: {evenAccum}, la suma de todos los números pares es: {oddAccum}.")
