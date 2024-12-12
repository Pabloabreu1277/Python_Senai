# #SEts
# # São conjuntos posso fazer uniao, intersecção e calculos dos conjuntos
#
# Set_conjunto = set()
#
# print(Set_conjunto)
# print(type(Set_conjunto))
#
# # set1 = (1,2,3,4)
# set1 = (4,67,867,23,5,768,9,3234,0)
#
# print(set1)
#
# for item in set1:
#     print(item)
#
#
# print(sum(set1))
# print(min(set1))
# print(max(set1))
#
#
# set_alf=("a","v","l","r")
# print(set_alf)
#
# set1={1,2,3,4}
# set2={5,6,7,8}
# #
# print(set1)
# print(set2)
# # # set2.add(10)
# # print(set2)
#
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
#
# quadrados = []
#
# for i in range(10):
#     quadrados.append(i**2)
#
# print(quadrados)
#
# quad1 = [numero **2 for numero in range(10)]
#
# print(quad1)
# pares=[]
#
# for i in range(100):
#     if i % 2==0:
#         pares.append(i)
#     else:
#         pass
# print(pares)
#
# # ou
# """memoria pares recebe =  uma variavel i quando para a variavel
#  entiver em um intervalo for i in range(100) se i for par atraves do resto da divisão igual a zero"""
#
# pares = [ i for i in range(100) if i % 2==0]
#
# print(pares)
#
# List_percent = [num /100 for num in range(100) if num in pares]
#
# print(List_percent)
#
# salarios = [5000, 6000, 4000, 1000, 4500]
#
# salarios_liquidos = [salario * 0.8 if salario > 6000 else salario * 0.9 for salario in salarios ]
# print(salarios)
# print(salarios_liquidos)
#
#
# # list compreention dentro do outro
#
# matriz = [[i+j for i in range(1,100,1)] for j in range(5)]
#
# print(*matriz, sep='\n')

#Shallow e deep copy

# a = 10
#
# b = a

# print(a==b)

a = [1,3,45,6]

b = a.copy()#So funciona para listas

print(a)
print(b)

b.append(7)
print(a,b)

# saber o local da memoria
print(id(a))
print(id(b))

