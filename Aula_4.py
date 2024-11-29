# AULA 04
# O que vamos fzer hoje?
# Revisão Atividade 3
# Operadores
# Matematicos, comparação, Logica

#Operadores matematicos
# retirar aspas para rodar codigo
"""
print(3176842354827356 + 623565487236492837)
print(7263875623948579284375209348 - 537298379823049238)
print(12*10**12 * 11*10**12)
print(1*10**8 / 1*10**7)
print(1*10**8 // 1*10**7)
print(100//30)
print(10000%300)
print(12**34)

"""

#Exercicios Terreno
#Vamos Calcular o valor de um terreno
# Vamos Receber o valor do metro quadrado m²

# retirar aspas para rodar codigo
"""
Valor_Metro_Quadrado = float(input("Digite o valor em R$ do m² de sua região de interesse:"))

print(Valor_Metro_Quadrado)
print(f"Valor digitado:{Valor_Metro_Quadrado}")
Area_Metro_Quadado = float(input("Informe a area do terreno em metros quadrados m²:"))
print(f"Valor digitado:{Area_Metro_Quadado}")

Valor_Terreno = Valor_Metro_Quadrado * Area_Metro_Quadado
print(f"O Valor do terreno será: R${Valor_Terreno:,.2f}")
"""
#Exercicio Baskara
# Importação da biblioteca SQRT para calcular raiz quadrada
import math
from math import sqrt

# Conficientes
a = int(input("Informe o valor de A:"))
b = int(input("Informe o valor de B:"))
c = int(input("Informe o valor de C:"))

delta = b **2 - 4 * a * c
x1 = -b + sqrt(delta) / 2 * a
x2 = -b - sqrt(delta) / 2 * a

print(f"As raízes da equação {a}x² + {b}x + {c} são: ")
print(f"S{x1, x2}")


