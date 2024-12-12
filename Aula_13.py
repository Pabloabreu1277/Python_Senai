# #Manipulação de arquivos TXT
# # Criação ou abertura de txt
# file = open('arquivo_aula13.txt','w')
#
# # pwd no terminal ve o caminho do projeto dica
# # escrever no arq
# file.write("oi mundo chama !!!")
# file.writelines(["\nVamos pra cima meu povo\n "])
#
# # with open('arquivo_aula13.txt','a') as file:
# #     file.write(input('escreva   '))
#
# with open('dragonballz','r') as file:
#     for linha in file.readlines():
#         print(linha.replace('\n','correcao'))
#         print(linha + f'tamanho linha:{len(linha)}\n')
#
# file.close()

# cadastro={}# inicio de uma criação de API para microserviços
# with open('Dados.txt','r') as file:
#     for linha in file.readlines():
#         chave, valor = linha.split(':')
#         cadastro[chave.replace('\n','')] = valor.replace('\n','')
# print(cadastro)
#
# Json dicionarios java script obj, utilizados em api's, aqr de text de dados no formato de dicionarios



