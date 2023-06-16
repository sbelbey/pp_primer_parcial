"""
Escribe un programa que calcule el área y el perímetro de un cuadrado 
y muestre los resultados (indicando cuál es cuál) por pantalla.
"""

lado = int(input("Ingrese la longitud de uno de los lados del cuadrado: "))

print("El área del cuadrado es:", lado*lado,
      "y su perímetro es:", lado*4, sep=" ")
