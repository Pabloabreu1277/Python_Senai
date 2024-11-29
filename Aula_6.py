#blocos de repetição
#Listas Tuplas e Bibliotecas

#FOR

# for cada_coisa in algum lugar:
#     Faça açguma coisa

# Palavra = "palavra bem grande"
# for letra in Palavra:
#     print(letra)
#

# conta = 0
# i = 0
# for i in range(10):
#     conta = i
#     print(i)
#     print(conta)

# #Exemplo com if
# pre = "WAKAWAKA"
#
# for i in range(100):
#     i=i+1#se eu não querer a contagem do zero
#     if i < 10:
#         print(f"{pre}0{i}")
#     else:
#         print(f"{pre}{i}")

# for i in range(0, 50, 2):
#     i=i+1
#     print(i)
#

# # Exemplo de o dobro do valor
# num = int(input("Entre com um valor: "))
#
# for i in range(1, num+1, 1):
# # for i in range(1, num, 1):
#     print(f"o dobro de {i} é {i * 2}")

# # for loop codigo 3
# numero = int(input("informe o numero que se deve apresentar a tabuada: "))
# print(f"vamos ver a tabuada do {numero}")
# for num in range(1, 11, 1):
#     print(num * numero)

# # For Loop – Código 4
# import time
# for i in range(10, -1, -1):
#     print( end=str(i))
#     time.sleep(1)
# print("\nDownload Concluido")

# # Loop While codigo 1
# contador = 0
# while contador < 15:
# #   contador = contador + 1
#     contador +=1 # forma mais pythonica de incrementar.
#     print(contador)


# # While Loop – Código 2
# import time
# tempo=0
# while tempo > -1:
#     print("\r", end=str(tempo))
#     time.sleep(1)
#     tempo -= 1

# # While Loop – continue e break - Código SENHA Fazer login
#
# acesso ='thiago_001'
# controle_acesso = False
# while not controle_acesso:
#     chave_acesso = input('Informe sua credencial: ')
#     if chave_acesso == acesso:
#         controle_acesso = True
#     else:
#         continue
# print('\nBem-vindo ao sistema.')

# #While Loop – Exemplo (Forca)
# palavra = input("Entre com a palavra: ").lower()
# jogo = ["_" for letra in palavra] # Cria uma lista com "_" para cada letra da palavra
# print("Vamos Jogar Forca!")
# print("\nPalavra Secreta:", " ".join(jogo))
# chances = 6
# letras_usadas = set()
# while chances > 0:
#     letra = input("Fale uma letra: ").lower()
#     if letra in letras_usadas:
#         print("Você já usou essa letra!")
#     else:
#         letras_usadas.add(letra)
#         if letra in palavra:
#             for i in range(len(palavra)):
#                 if palavra[i] == letra:
#                     jogo[i] = letra
#             print("".join(jogo))
#         else:
#             chances -= 1
#             print(f"Essa letra não tem, sobraram {chances} chances.")
#     if "_" not in jogo: # Verifica se todas as letras foram descobertas
#         print("Você acertou!")
#         break