"""Crie um sistema de cadastro de usuario contendo inputs de informações
do usuario e as confirmações de cada dado salvo """
# Nome
# Idade
# Cidade
# Estado

#Bibliotecas importação
import time

#Programação
print("SISTEMA DE CADASTRO DE USUARIOS")
print("-"*32)

Nome = input("Digite seu nome completo: ").title()
print(Nome)

Idade = input("Digite sua Idade: ")
print(Idade)

Cidade = input("Digite sua Cidade: ").upper()
print(Cidade)

Estado = input("Digite seu Estado: ").upper()
print(Estado)

# Confirmação do cadastro
print("Carregando...")
time.sleep(5)

print("Dados Cadastrados com Sucesso !!!")
print(f"""
Usuario= {Nome}
O usuario tem a idade= {Idade}
Mora na cidade= {Cidade}
No estado= {Estado}

OBRIGADO :D
""")
