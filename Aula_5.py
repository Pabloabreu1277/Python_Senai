#Operadores logicos True False Bolean

# print(12>10 and 3==3)
# print(12>10 or 3==3)
#
# print(not True)
# print( not 12>10 and 3==3)
# print(not 10 % 2 != 0 or 3> 24)


#Estruturas de Decisão - Keywords if,elif e else
"""
n=0
for n in range (0,10):
    n = n+1
    if n >= 10:
        print("acertou")
    else:
        print("errou")
"""

"""
# exemplo professor
produto="LED 6W"
unidades_produto = int(input(f"Informe a quantidade do produto {produto}: "))
print(unidades_produto<=500)
if unidades_produto <= 500:
    print(f"comprar mais produto: {produto} ")
else:
    print(f"Estoque ok não precisa comprar mais produtos: {produto}")
"""
# --------------------------------------------------------------------
"""
# Controle de estoque
Produto_Led_6W = 1000
print(f"Estoque atual: {Produto_Led_6W}")
Alarme_estoque = 100
produto="LED 6W"
Retirada_Estoque = 0
print("Controle de movomentação de Estoque")
Retirada_Estoque=int(input(f"Quantidade de retirada do produto: {produto} ?"))
Produto_Led_6W = Produto_Led_6W - Retirada_Estoque
print(f"Sua solicitação: {Retirada_Estoque}")
print(f"Saldo atual: {Produto_Led_6W}")

if (Produto_Led_6W <= 100) and (Produto_Led_6W >= 0):
    print(f"ALERTA!!! Voce atingiu o limite minimo de 100 unidade")
    print(f"Seu saldo é: {Produto_Led_6W}")
    print("Solicitar compra")
elif Produto_Led_6W < 0:
    print("Solicitação não permitida voce não tem mais estoque")
    print(f"Seu saldo é: {Produto_Led_6W}")

"""
# Decisão Aninhada - Código

nome = input("Entre com seu nome: ").title()
idade = int(input("Entre com sua idade: "))
print(f"\n Oi meu nome é {nome} etenho {idade} anos de idade.\n")

if idade >= 65:
    cnh = input("Possui CNH ? (Responda s ou n): ")

    print(f"{nome} já é bastante experiente.")
    if cnh == 's':
        print("Voce deve renovar a cnh a cada 5 anos")
    else:
        pass
elif 65 > idade >= 18:
    print(f"{nome} é maior de idade.")
    cnh = input("Possui CNH ? (Responda s ou n): ")

    if cnh == 's':
        print("Voce deve renovar a cnh a cada 5 anos")
    else:
        pass
else:
    print(nome + ' é ' + 3 * 'Jovem ainda, ')





