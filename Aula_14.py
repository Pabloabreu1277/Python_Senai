# #tratamento de exceções
# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Não podemos dividir por zero!!!")
# except ValueError:
#     print("Um erro aconteceu, so podemos dividir por numeros!!!")
# finally:# se der erro ou não ele sempre execulta
#     print("Execulta sempre")

#
# while True:
#
#     nome_arquivo = input("Nome do arquivo desejado, para sair aperte a tecla enter: ")
#     if nome_arquivo:
#         try:
#             with open(f'{nome_arquivo}.txt', 'r') as file:
#                 print(file.read())
#         except FileNotFoundError:
#             print("Esse arq não existe, tente de novo!")
#
#         finally:
#             print("Sistemas de arquivo")
#     else:
#         break


# #usando como uma função
# def ler_arquivo(nome_arquivo):
#
#     # nome_arquivo = input("Nome do arquivo desejado:")
#     try:
#         with open(f'{nome_arquivo}.txt', 'r') as file:
#             print(file.read())
#     except FileNotFoundError:
#         print("Esse arq não existe, tente de novo!")
#     finally:
#         print("Sistemas de arquivo")
#
#
# print(ler_arquivo('dados'))


# def division (a: int, b: int) -> float | None:
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Não podemos realizar uma divisão por zero")
#     except TypeError:
#         print("Apenas numeros")
#
# print(division(10,2))
# division(10, 0)
# division(10, 'a')

# def division (a: int, b: int) -> float | None:
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Não podemos realizar uma divisão por zero")
#     except Exception:
#         raise ValueError ("ERRO FATAL")
#
# print(division(10,2))
# division(10, 0)
# division(10, 'a')