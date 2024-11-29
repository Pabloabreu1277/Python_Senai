
# Operadores – Exercício 1


#sabendo que: Formulario Raio=r, Area=pi*r, diametro=2*r
# Crie um programa que receba o valor do raio de uma circunferencia e imprima
#Calcule a area
#calcule o perimetro
#calcule o diametro

import math as mt

# ou pi da biblioteca math

print("Exercicio 01")
print("_________________________________________________\n")

Raio = float(input("Digite o valor do raio :"))

Perimetro = 2*mt.pi*Raio
print(f"Valor do perimetro calculado é: {Perimetro}")

Area_Circ = mt.pi * Raio
print(f"Valor da area calculada é: {Area_Circ}")

Diametro = 2 *Raio
print(f"VaLor do Diametro Calculado é: {Diametro}\n")


# Operadores – Exercício 2
# Crieum codigo que receba a temperatura em Celcius e calcule:
#Temperatura em FArenheit
# Temperatura em Kelvin
#Formulario: F=(C*1.8)+32, K=C+273,15
print("Exercicio 02")
print("_________________________________________________\n")

Temp_Celcius = float(input("Digite uma temperatura em °C:"))

#Calculos

Temp_Farenheit = (Temp_Celcius*1.8)+32
print(f"A temperatura em Farenheit é: {Temp_Farenheit}°F")


Temp_Kelvin = Temp_Celcius + 273.15
print(f"A temperatura em Kelvin é: {Temp_Kelvin}°K")


# Operadores – Exercício 3
#Crie um programa que receba as 4 notas dos bimestres de um aluno
#Calcule a media de notas desse ano
#Print a msg da media final desse aluno

print("Exercicio 03")
print("_________________________________________________\n")

print("OLÁ Sou Sua calculadora de notas, Vamos começar!!!\n")
Nome_Aluno = input("Informe o nome do aluno:")

#Nota_01 = float(input("Informe a nota do 1° Bimestre: "))
#Nota_02 = float(input("Informe a nota do 2° Bimestre: "))
#Nota_03 = float(input("Informe a nota do 3° Bimestre: "))
#Nota_04 = float(input("Informe a nota do 4° Bimestre: "))
Nota_Aluno = [ ]
for i in range(1,5):
    Nota_Aluno_ESC = int(input(f"Escreva uma nota{i}°Bimestre: "))
    Nota_Aluno.append(Nota_Aluno_ESC)
    print(Nota_Aluno)

Nota_Aluno_calc = Nota_Aluno[1]+Nota_Aluno[2]+Nota_Aluno[3]+Nota_Aluno[4]
print(Nota_Aluno_calc)

#print(f"{Nome_Aluno} sua média final foi de {Media_Final:.2f}")