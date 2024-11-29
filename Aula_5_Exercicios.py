# Estrutura de Decisão – Exercício 1
# Utilizando os conceitos aprendidos até aqui,
# faça um programa que pede duas notas de um aluno,
# em seguida ele deve calcular a média do alunoe dar o seguinte resultado:
# aprovado media >= 7
# reprovado media < 7
# aprovação com exelencia media == 10

print("Resistencias dos materiais - Calculadora de Média Final" )
Nome = input("Digite o nome do aluno: ")
Nota_01 = float(input("Digite a nota da P1: "))
Nota_02 = float(input("Digote a nota da P2: "))

Media_final = (Nota_01 + Nota_02)/2

if Media_final >= 7:
    print(Media_final)
    Status = "Aprovado Parabens "
    print(f"Sr(a) {Nome} voce esta {Status} ")
elif Media_final == 10:
    print(Media_final)
    Status = "Aprovado com Maestria :D Parabens"
    print(f"Sr(a) {Nome} voce esta  {Status} ")
else:
    print(Media_final)
    Status =("Reprovado !!! :C tente denovo, Solicite a P3")
    print(f"Sr(a) {Nome} voce esta {Status} ")


##################################################

# Estrutura de Decisão – Exercício 2
# Programa que compara os lados de um triangulo
# Identifique o tipo da forma do triangulo
# Triangulo equilatero 3 lados iguais
# isosceles 2 lados iguais
# triangulo tres lados diferentes

print("CLASSIFICAÇÃO DE GEOMETRIA TRIANGULAR")
print("-----------------------------------------")

Lado_A = float(input("Digite o valor do lado A de sua geometria: "))
Lado_B = float(input("Digite o valor do lado B de sua geometria: "))
Lado_C = float(input("Digite o valor do lado C de sua geometria: "))
# Identifica se é um triangulo
if (Lado_A==0) or (Lado_B == 0)  or (Lado_C == 0):
    print("Essa geometria não é um Triangulo!!!")
elif ((Lado_A+Lado_B) > Lado_C) or ((Lado_A+Lado_C) > Lado_B):
    print("Sua forma geometrica é um triangulo")

    if (Lado_A == Lado_B) and Lado_C == Lado_B:
        print(f"Esse Triangulo é do tipo EQUILÁTERO, {Lado_A:.2f}x{Lado_B:.2f}x{Lado_C:.2f}")

    elif (Lado_A == Lado_B) or Lado_C == Lado_B or Lado_C == Lado_A :
        print(f"Esse Triangulo é do tipo ISÓSCELES, {Lado_A:.2f}x{Lado_B:.2f}x{Lado_C:.2f}")

    elif (Lado_A != Lado_B) or Lado_C != Lado_B or Lado_C != Lado_A :
        print(f"Esse Triangulo é do tipo ESCALENO, {Lado_A:.2f}x{Lado_B:.2f}x{Lado_C:.2f}")

    else:
        pass


else:
    pass

################################################################################

#Estrutura de Decisão – Exercício 3
# crie um programa que calcule o salario liquido do funcionario
#Até 2000 isento imposto
# de R$2001 a R$3500 imposto 10 %
# de 3501 a 5000 imposto de 15%
# acima de 5000 imposto 20%

print("CALCULADORA DE SALARIO LIQUIDO")

Salario_Bruto = float(input("Digite o seu salario bruto: "))

if Salario_Bruto > 5000:
    print(f"Seu Salario Bruto é: R$ {Salario_Bruto} ")
    print("O imposto cobrado sera de: 20% ")
    Salario_Liq = Salario_Bruto * 0.80
    Imposto = Salario_Bruto * 0.20
    print(f"Seu Salario liquido é: R${Salario_Liq}")
    print(f"O imposto cobrado será de: R$ {Imposto}")

elif (Salario_Bruto >= 3501) and (Salario_Bruto<=5000):
    print(f"Seu Salario Bruto é: R$ {Salario_Bruto} ")
    print("O imposto cobrado sera de: 15%")
    Salario_Liq = Salario_Bruto * 0.85
    Imposto = Salario_Bruto * 0.15
    print(f"Seu Salario liquido é: R${Salario_Liq}")
    print(f"O imposto cobrado será de: R$ {Imposto}")

elif (Salario_Bruto >= 2001) and (Salario_Bruto<=3500):
    print(f"Seu Salario Bruto é: R$ {Salario_Bruto} ")
    print("O imposto cobrado sera de: 10%")
    Salario_Liq = Salario_Bruto * 0.90
    Imposto = Salario_Bruto * 0.10
    print(f"Seu Salario liquido é: R${Salario_Liq}")
    print(f"O imposto cobrado será de: R$ {Imposto}")
else:
    print(f"Seu Salario Bruto é: R$ {Salario_Bruto} ")
    print("O imposto cobrado sera de: 0%")
    Salario_Liq = Salario_Bruto
    print(f"Seu Salario liquido é: R${Salario_Liq}")