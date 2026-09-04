"""""
def mercado(Nome="Mercado Padrão", endereço="Rua sla, 456", telefone="40028922"):
    Nome = input("Digite o nome do mercado: ")
    endereço = input("Digite o endereço do mercado: ")
    telefone = input("Digite o telefone do mercado: ")
    break_line = "-"*50
    print(break_line)
    print(f"Nome do mercado: {Nome}")
    print(f"Endereço: {endereço}")
    print(f"Telefone: {telefone}")
    
    

def funcionarios(nome="Alex", sexo="Masculino", idade="21"):
    Nome = input("Digite o nome do funcionário(a): ")
    Sexo = input("Digite o sexo do funcionário(a): ")
    idade = input("Digite a idade do funcionário(a): ") 
    
    print(f'Nome do funcionário: {Nome}')
    print(f'Sexo: {Sexo}')
    print(f'Idade: {idade}')
    break_line = "-"*50
    print(break_line)
    
    
def cliente(nome="cliente ", sexo="Masculino", idade="21"):
        Nome = input("Digite o nome do cliente: ")
        Sexo = input("Digite o sexo do cliente: ")
        idade = input("Digite a idade do cliente: ") 
        
        print(f'Nome do cliente: {Nome}')
        print(f'Sexo: {Sexo}')
        print(f'Idade: {idade}')
        break_line = "-"*50
        print(break_line)
    

funcionarios = funcionarios()
mercado = mercado()
cliente = cliente()
    """
    
    
    
'''    def Uci(Nome = 'Uci cinemas', Localização = 'Shopping Parangaba', Preço = '24'):
        
        Preço = input('Digite o valor que deseja pagar:')
    print('Sua compra foi realizado')
    
    
    cinema = cinema() 
         
        '''
'''class Petshop:

    def __init__(self, animal, nome, idade, raca):
        self.animal = animal
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def mostrar(self):
        print(f"Espécie: {self.animal}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Raça: {self.raca}")


animal1 = Petshop("cachorro", "Bruce", "3 anos", "Golden")

animal1.mostrar()'''
'''

        carro1 = carro("toyota","corolla",2020,"preto")
        carro2 = carro()
    
class animal:
    
    def __init__(self,nome,raça,idade):
        self.nome = nome
        self.raça = raça
        self.idade = idade
    def detalhes(self):
        return f"{self.nome}{self.raça}{self.idade}"
    
animal1=animal('bruce','pastor alemão','3')
print(animal1.detalhes())   '''
'''
class carro:
    def __init__(self,marca,modelo,ano,cor):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        
    def detalhes(self):
        return f'{self.marca}{self.modelo}{self.ano}{self.cor}'
        
carro1 = carro('toyota','corolla','2020','preto')
print(carro1.detalhes())
'''
class petshop:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def detalhes(self):
        def apresentar(self):
            print(f"o nome dele é{self.nome}")
            print(f"a idade dele é{self.idade}")
class cachorro(petshop):
        def __init__(self,nome,idade,raça):
            super().__init__(nome,idade)
            self.raça = raça
cachorro1 = cachorro('bruce',3,'pastor alemão')
print(cachorro1.nome)
print(cachorro1.idade)
print(cachorro1.raça)

cachorro1.apresentar()
    hiuri