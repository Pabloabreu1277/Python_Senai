# # Atividade 07
# # exercicio 1
#
# lista = [1,2,3,4,5,6,7,8,9,765]
#
# lista_quadrado = \
#     list(map(lambda x: x**2, lista))
# print(lista_quadrado)
#
# lista_filtrada= list(filter(lambda x: x%2 != 0, lista_quadrado))
# lista_filtradapar= list(filter(lambda x: x%2 == 0, lista_quadrado))# extra
#
# print(lista_filtrada)
# print(lista_filtradapar)
#####################################################################################
# # exercicio 2
#
# palavras = ['carro', 'game', 'cachorro','amor', 'churrasco']
#
# palavras_maiusculas = list(map(lambda p: p.upper(), palavras))
# print(palavras_maiusculas)
#
# palavras_maiores = list(filter(lambda p: len(p) > 5, palavras_maiusculas))
# print(palavras_maiores)
#
#######################################################################################

# #exercicio 3
#
# lista_z = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
#
# lista_z_filter = list(filter(lambda z: z>0, lista_z))
# print(lista_z_filter)
#
# lista_z_map = list(map(lambda z: z**2, lista_z_filter))
# print(lista_z_map)

########################################################################################
# # exercicio 4
#
# Nomes_aleatorios = ['carro', 'game', 'cachorro','amor', 'churrasco']
#
# Nomes_Aleatorio_Primeiro = list(map(lambda n: n[0].upper(),Nomes_aleatorios))
# print(Nomes_Aleatorio_Primeiro)
#######################################################################################

# exercicio 5

# Funcionarios = [
#     {"nome":"anild","salario": 1000},
#     {"nome":"bosnio","salario":2000},
#     {"nome":"carlos","salario": 3000},
#     {"nome":"daniels","salario": 4000}
# ]
#
#
# print(Funcionarios)
#
# Funcionarios_aumento = list(map(lambda s: round(s ['salario'] * 1.1, 2), Funcionarios))#s seria meu dicionario
# # Funcionarios_aumento = dict(map(lambda s: s.update(round(float(s {'salario'}) * 1.1,2)), Funcionarios))
#
# print(Funcionarios_aumento)
