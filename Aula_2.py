# #TODO: Revisar codigos pos aula 02
# print("Hello World!!!")
# # ctrl / comentarios
#
# """criação de variavel, eu crio uma variavel,
#  alocando uma posição de momeria, referencia Caixa referencia uma
#   posição da memoria aleatoria e o valor dela é 10"""
#
# Caixa = 10
# print('Caixa =', 10)
#
# #Mosta a posição da memoria
# print(id(Caixa))
#
# Caixa = Caixa + 10**51.5
#
# print('Agora o meu valor da caixa é =',Caixa)
#

Nome = ('Pablo ricardo')
Idade = 30
Altura = 1.73
Vivo = True

print(Idade + 10)
print(type([Nome,Idade,Altura,Vivo]))
print(type(Nome))
print(type(Idade))
print(type(Altura))
print(type(Vivo))


print(Nome,Idade,Altura,Vivo,sep='___', end='___Finish')

#Concatenação de Strings

print("opre"+" e ai man ?")

print("oi meu nome é: "+ Nome +" Tenho "+str(Idade)+" anos de Idade")

# Fstring forma pythonica de escrever mensagens

print(f"oi, meu nome é {Nome} eu tenho {Idade} anos de Idade")

Nome_Usuario = input("Digite sem primeiro nome (Nome): ")

print(f"Nome do Usuario Cadastrado: {Nome_Usuario}")
