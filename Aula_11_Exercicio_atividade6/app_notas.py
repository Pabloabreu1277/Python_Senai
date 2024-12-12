from Notas import media_notas

def main():
    while True:
        Nota_01 = float(input("Informe a nota do 1° Bimestre: "))
        Nota_02 = float(input("Informe a nota do 2° Bimestre: "))
        Nota_03 = float(input("Informe a nota do 3° Bimestre: "))
        Nota_04 = float(input("Informe a nota do 4° Bimestre: "))
        notas = (Nota_01,Nota_02,Nota_03,Nota_04)
        media = media_notas(Nota_01,Nota_02,Nota_03,Nota_04)
        if media >= 5:
            print("Aluno Aprovado")
            print(media)
            break
        else:
            print("Aluno Reprovado")
            print(media)
            print("Digite notas de outro aluno:\n")
            continue
        print(media)


if __name__ == '__main__':
    main()