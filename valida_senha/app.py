from senha import Valida_Senha

def main():
    while True:
        senha = input("""
        Digite sua senha com os seguintes itens:
        
        --Letra maiuscula
        --Letra minuscula
        --Caracteres especiais
        --tamanho de 8 digitos
        """)
        if Valida_Senha(senha):
            print("senha forte")
            break
        else:
            print('Senha fraca')
            continue
    print('Bem vindo(a) ao sistema')

if __name__ == '__main__':
    main()
