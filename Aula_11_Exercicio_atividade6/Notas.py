#Refatorar exercicio 3 da aula 4, utilizando funções e tipagem para app
# Operadores – Exercício 3
#Crie um programa que receba as 4 notas dos bimestres de um aluno
#Calcule a media de notas desse ano
#Print a msg da media final desse aluno
#
# print("Exercicio 03")
# print("_________________________________________________\n")
#
# print("OLÁ Sou Sua calculadora de notas, Vamos começar!!!\n")
# Nome_Aluno = input("Informe o nome do aluno:")
#
# Nota_01 = float(input("Informe a nota do 1° Bimestre: "))
# Nota_02 = float(input("Informe a nota do 2° Bimestre: "))
# Nota_03 = float(input("Informe a nota do 3° Bimestre: "))
# Nota_04 = float(input("Informe a nota do 4° Bimestre: "))
#
# Media_Final = (Nota_01+Nota_02+Nota_03+Nota_04)/4
#
# print(f"{Nome_Aluno} sua média final foi de {Media_Final:.2f}")
#Função def
#Entrada 4 notas
#resultado media de notas
#descrição dos parametros
#Chamada da função main
from fontTools.misc.cython import returns


def media_notas(Nota01,Nota02,Nota03,Nota04) -> float:
    """
    :param Nota01: 0 a 10 ou 0 a 100, pode usar numeros quebrados 7.6 ou 8.67 segue esse padrão nas outras etradas
    :param Nota02:
    :param Nota03:
    :param Nota04:
    :return: Media das notas
    """
    media = (Nota01+Nota02+Nota03+Nota04)/4

    return media

# notas = media_notas(10,2,9,10)
# print(notas)

# def test():
#     ai=int(input("entre com um valor"))
#     y = ai + 1
#     return y
#
# a = test()
# print(a)