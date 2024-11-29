# Loops – Exercício 1
import time

# Crie um programa que:
# -Receba um número do usuário;
# -Apresente a tabuada desse número.
print("Loops – Exercício 2")
print("TABUADA AUTOMATICA")
for i in range(30):
    print(end = str("°"))
    time.sleep(0.05)
Numero_tabuada = int(input("\nDigite um numero da tabuada desejada: \n"))
for i in range(0, 10, 1):
    i +=1
    Tabuada = Numero_tabuada * i
    print(f"{Numero_tabuada} X {i} = {Tabuada}\n")

# Loops – Exercício 2

# Crie um programa que seja um somador de despesas simples:
# -Receba a quantidade de despesas;
# - Faça a soma de cada despesa em uma variável;
# - Ao final, apresente o valor total da despesa.
# O output deve ser similar ao exemplo abaixo:
print("Loops – Exercício 2")
Dispesas_Num = int(input("Informe a quantidade de compras realizadas: "))
i = 0
Divida = 0
for i in range(Dispesas_Num):
    i+=1
    Compras_incre=float(input(f"Digite o valor da compra {i}: "))
    Divida = Divida + Compras_incre

print(f"O valor da sua divida total será: {Divida}\n")

# Usando o loop While

Dispesas_Num = int(input("Informe a quantidade de compras realizadas: "))
Divida = 0
while Dispesas_Num > 0:
    Dispesas_Num = Dispesas_Num - 1
    Compras_incre = float(input(f"Digite o valor da compra: "))
    Divida = Divida + Compras_incre
print(f"O valor da sua divida total será: {Divida}\n")

# Loops – Exercício 3
# Crie um sistema de banco simples, com as seguintes opções:
# -Menu com 1: Depósito, 2: Saque e s: Sair
# - A aplicação deve parar quando o cliente escolher 's'
# - Ao final, imprima uma mensagem com o saldo final do cliente.
print("Loops – Exercício 3")
print("ABREU VASCONCELOS BANK")
for i in range(30):
    print(end = str("°"))
    time.sleep(0.05)
Menu_Banco = int(input("\nEscolha a opção a seguir:\n ---1-Deposito\n ---2-Saque\n ---3-Sair\n"))
Saldo = float(1000000)
while Menu_Banco != 3:
    if Menu_Banco == 2:

        print(f"Seu saldo atual é: R${Saldo:.2f}\n")
        Saque = float(input("Quanto deseja sacar?\n "))
        if Saque > Saldo:
            print(f"Voce não tem saldo disponivel R${Saldo}, tente novamente: \n ")
            Menu_Banco = int(input("Escolha a opção a seguir:\n ---1-Deposito\n ---2-Saque\n ---3-Sair\n"))
        else:
            Saldo = Saldo - Saque
            print(f"Seu saldo atual é: R${Saldo:.2f}\n")
            Menu_Banco = int(input("Escolha a opção a seguir:\n ---1-Deposito\n ---2-Saque\n ---3-Sair\n"))

    elif Menu_Banco == 1:
        print(f"Seu saldo atual é: R${Saldo:.2f}\n")
        Deposito = float(input("Quanto deseja Depositar?\n "))
        Saldo = Saldo + Deposito
        print(f"Seu saldo atual é: R${Saldo:.2f}\n")
        Menu_Banco = int(input("Escolha a opção a seguir:\n ---1-Deposito\n ---2-Saque\n ---3-Sair\n"))

