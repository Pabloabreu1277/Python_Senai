# Aplicativo para rodar um identificador de numeros primos
from primos import primo

def main():
    while True:
        numero = int(input("N: "))
        if numero == 0:
            break
        elif primo(numero) >= 2:
            print(f"{numero} não é primo!!!")
        else:
            print(f"{numero} é primo!")

if __name__ == '__main__':
    main()