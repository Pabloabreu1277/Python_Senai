# Orientação a objeto
#classe - Generico
#Objeto - instancia da classe
#Atributo - Caracteristicas do objeto
#metodo - ações execução

# instancia criar objeto
# herança é mecanismos que permite criar novas classes
# polimorfismo

# # exemplo
#
# class Cachorro:
#     # contrutora de objeto
#
#     def __init__(self,nome,raca,cor,idade,porte):#podemos tipar nome:str
#         # atributos da classe
#         self.nome = nome
#         self.raca = raca
#         self.cor = cor
#         self.idade = idade
#         self.porte = porte
#
# pipoca = Cachorro('Pipoca', 'shitsu','branco',1,'pequeno')#pipoca é objeto
#
# print(pipoca.nome)
# print(pipoca.raca)
# print(pipoca.cor)
# print(pipoca.idade)
# print(pipoca.porte,'\n')
#
# fred = Cachorro('Fred','shitzu','branco',1,'pequeno')
#
# print(fred.nome)
# print(fred.raca)
# print(fred.cor)
# print(fred.idade)
# print(fred.porte,'\n')

# Superclasse
class Carro:
    marca:str
    modelo:str
    cor:str
    ano:int
#construção
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"{self.modelo} Ligado!!")
#metodos ações
    def desligar(self):
        self.ligado = False
        print(f"{self.modelo} Desligado!!")
#Metodos estaticos
    @staticmethod
    def troca_pneu():
        print('trocando o pneu')

    def liga_farol(self):
        escuro = input("Agora é dia ou é noite, responda N=noite e D=dia").upper()
        if escuro == "N":
            print('Farol alto ligado!')
        elif escuro == "D":
            print('Farol baixo e milha ligado!')
        else:
            print('Farol com defeito!!!')

# Herança
class Caminhonete(Carro):
    tamanhoCarroca:int

    def __init__(self,tamanhoCarroca,marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)#link de outra classe
        self.tamanhoCarroca = tamanhoCarroca

    def carroceria(self):
        carrocaCaminhonet = input("Carroceria Aberta ou Fechada, responda A=aberta, F=fechada, aperte enter para sem carroceiria").upper()
        if carrocaCaminhonet == "A":
            print('Carroceria Aberta!')
        elif carrocaCaminhonet == "F":
            print('Carroceria Fechada!')
        else:
            print('Sem carroceiria')


Carro_01 = Carro('Renault', 'clio', 'prata', '2012')

print(Carro_01.modelo)
print(Carro_01.ligado)
Carro_01.ligar()
print(Carro_01.ligado)
Carro_01.desligar()
print(Carro_01.ligado)
# Carro_01.troca_pneu()
# Carro_01.liga_farol()

# Polimorfismo com super()
Carro_02 = Caminhonete(1000,'mercedes','tratos','preto','2024')

print(Carro_02.modelo)
print(Carro_02.ligado)
Carro_02.ligar()


