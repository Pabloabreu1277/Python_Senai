# Dicionários – Código 4

# While true analisa a condição do produto tendo a informação do nome se caso nao tiver pulo para else e para o programa
estoque={}

print('\n - Vamos atualizar o estoque do sistema - ')
while True:
    produto= input('Informe o nome do produto (ou enter para sair): ')
    if produto:
        quantidade = int(input(f'Quanto de {produto} temos em estoque: '))
        estoque[produto] = quantidade
        continue
    else:
        break

print("\n -Resumo do estoque- ")
if len(estoque)> 0:
    for prouto, quantidade in estoque.items():
        print(f'{produto}: {quantidade} unidades.')
else:
    print('O estoque esta vazio!!!')
    print(f"\n Temos um total de {sum(list(estoque.value()))} produtos no estoque.")
