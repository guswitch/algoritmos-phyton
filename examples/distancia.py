import sys
import os
import math

print("Distancia entre dois pontos")

x1, y1 = input('Entre com o ponto 1 (x1, y1): ')
x2, y2 = input('Entre com o ponto 2 (x2, y2): ')

res = math.sqrt(pow((float(x1)-float(x2)), 2) + pow((float(y1)-float(y2)), 2))

os.system('clear')

print('pontos p1 - x1: ' + x1 + ' y1: ' + y1)
print('pontos p2 - x2: ' + x2 + ' y2: ' + y2)
print('Distancia entre p1 e p2: ' + res.__str__())
