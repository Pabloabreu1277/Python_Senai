# # Def funçoes para fazer no pyton vc define a função def nome da função logica (variaveis, a e b):
# from functools import total_ordering
#
# from fontTools.misc.cython import returns
#
#
# # função def
#
# def exp(base: int | float, expoente: int | float) -> float:
#     return base ** expoente
#
# a = 10
# b = 2

# calculo_exp = exp(a, b)
# ou
# calculo_exp = exp(base=a, expoente=b)
# print(calculo_exp)
# Exp_natural = exp(2,2.1232342352)
# print(Exp_natural)
#
# base = int(input("Digite o valor da base: "))
# expoente= int(input("Digite o valor do expoente: "))
#
# ex = exp(base,expoente)
# print(ex)

# def exp1(base: 10,expoente:int | float) -> float:
#     return base ** expoente
#
# base = 11
# expoente=2
# # ex = exp1(1,expoente) metodo errado de usar os argumentos
# print(ex)
#
##Parametros da função
#
# def exp(base: int | float, expoente: int | float) -> float:
#     """
#     Função que faz o calculo de exponencioação:
#     :param base = valor da base da exponenciação como por exemplo base 10^x
#     :param expoente = Valor dedicadpo a ser o expoente de nossa potencia como por exemplo x^2
#     :param resultado = Sera o calculo da uniao desses dois valores 10^2
#
#     """
#     return base ** expoente


# *Args e Kagrs se comporta omo uma tupla
# problema para 10 entradas
# def somaerro(a,b,c,d) -> int:
#     """
#     :param a:
#     :param b:
#     :param c:
#     :param d:
#     :return:
#     """
#     return a+b+c+d
#
# def soma(*args):
#     return sum(args)
#
# results= soma(1,2,3,4,5,6,7,8,9,10)
#
# print(results)



## Parametros kwargs
#
# def Notas(**kwargs):
#     """
#     :param kwargs:
#     :return:
#     """
#     print(kwargs.values())
#     print(kwargs.keys())
#     for chave, valor in kwargs.items():
#         print(f"{chave} -> Nota:{valor}")
#
#     # return kwargs nem toda função retorna alguma coisa
# #     kwargs se comporta como um dicionario de chaves e valores
#
# Notas(pablo=10,ana=10,pipoca=10)

#REFATORANDO Aula_8_exemplo_dicionario

def Estoque(**kwargs):
    """

    :param kwargs:
    :return:
    """
    print("Vamos atualizar o estoque do sistema!!!\n")

    # estoque = {}
    print('\n-Vamos atualizae o estoque no sistema-')
    for produto, quantidade in kwargs.items():
        print(f'{produto}: {quantidade} unidades.')
    Estoque, total_produtos = sum(kwargs.values())

    return  kwargs, total_produtos

    #     produto = input('Informe o nome da produto (ou enter para sair): ')
    #     if produto:
    #         quantidade = int(input(f"Quanto de {produto} temos em estoque: "))
    #         estoque [produto] = quantidade
    #         continue
    #     else:
    #         break
    #
    # print('\n-Resumo do estoque-')
    # if len(estoque) > 0:
    #     for produto, quantidade in estoque.items():
    #         print(f'{produto}: {quantidade} unidades.')
    #     print(f'\nTemos um total de {sum(list(estoque.values()))} produtos no estoque.')
    #
    #
    # else:
    #     print('0 estoque está vazio.')