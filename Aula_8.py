# #Listas, tuplas, dicionarios e sets
# #in place metodo que age no objeto e não retorna nada
#
# # Listas
# lista_1 = [1,2,3,4,5,6,7]
#
# print(len(lista_1))
#
# print(lista_1[1:4])
#
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print (sum(numeros))
# print (max (numeros))
# print(min (numeros))
#
# # Matrizes
#
# matriz = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
#
# print(matriz)
#
# for i in matriz:
#     for j in i:
#         print(i)
#         print(j)
#
# lista_2=[8,9,10]
# print(lista_1 + lista_2)
#
# total = sum(lista_1+lista_2)
# print(total)
#
# frutas=["mamao", "maça", "uva", "laranja", "kiwi"]
# print(frutas)
# frutas.append("melancia")
# print(frutas)
# frutas.extend(["abacate", "limão","graviola"])
# print(frutas)
# frutas.insert(0, "Tangerina")
# print(frutas)

# # Listas – Código 3
# ultima_fruta = frutas.pop()
# print(ultima_fruta)
# print(frutas)
# frutas.sort(reverse=True) #não consigo guardar o resultado em outr variavel
# frutas_r=frutas.reverse()
# print(frutas_r)
# frutas.sort()
# print(frutas)
# print (frutas.index('maça'))
#
# # substituir
# frutas[1] = "guarana"
# print(frutas)
#
# # remover itens que sei o registro
#
# frutas.remove("guarana")
# print(frutas)

# #Tuplas
#
# tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(tupla_numeros[0])
# print(tupla_numeros [1:5])
# print(tupla_numeros[::-1])
# for item in tupla_numeros:
#     print(item)
#
# tupla = list(tupla_numeros)
# print(tupla)
#
# print(sum(tupla_numeros))
# print(max(tupla_numeros))
# print(min(tupla_numeros))
#
# tupla = ("Valor_01", "Valor_02","Valor_03")
#
# v1,v2,v3 = tupla
#
# print(v1)
# print(v2)
# print(v3)
# print(tupla)
#
# lista=list(range(1,200,1))
# print(lista)
#
# print(list(enumerate(lista)))
#
# for index, valor in enumerate(lista):
#     print(index, valor)
#
##Dicionario

# Cadastro_Canil = {1:"Cachorro",2:"gato", 3:"papagaio", 4:"lontra", 5:"Jabuti"}
#
# print(type(Cadastro_Canil))
# print(Cadastro_Canil[2])
# Cadastro_Canil[3] = [1,2,3]
# print(Cadastro_Canil)
# Cadastro_Canil[6] = "Macaco"
# print(Cadastro_Canil)

# #Funções do dicionario
# dict_valores = {"a": 1, "b": 2, "c": 3, "d": 4}
# print(dict_valores.keys())
# print(dict_valores.values())
# print (dict_valores.items())
#
# #ORM
# Docts = {
#     1:{'nome':'pablo','RG':163722762746,'CPF':52369823576 },
#      2: {'nome': 'Ana', 'RG': 16372276, 'CPF': 52369576}
#  }
#  print(Docts)
#
# print(Docts[1]['RG'])
#
# for chave, valor in Cadastro_Canil.items(): # desempacotar um dicionario com seus itens
#     print(chave, "--->", valor)
#
# for valor in Docts.values():
#     print(valor)
#     for info in valor.values():
#         print(info)

# update e remoção

# for registro in Docts.values():
#
#     del registro['RG']
#     print(registro)
#     # registro['Nacimento'] = input("Seu ano de nacimento: ")
#     registro.update({'Ano': input("Seu ano de nacimento: "), 'CEP':input("Seu cep: ")})
#
# print(Docts)

# print((Docts[1]['nome'],Docts[2]['nome']))

