#O que é POO?
#Programa orientada a objeto, organiza o código em objetos euq são entidade sque possuem atributos (dados) e métodos (funções).
#Beneficios: código mais organizado, facilita manuntenção e reaproveitamento e essencial para projetos grandes e frameworks

#Classes e objetos

#Classes é como um molde ou modelo que define atributos e comportamentos.
#Exemplo: um molde de carro, sem representar um carro especifico
class carro:
    pass

#Objeto é uma instancia da classe, ou seja, um carro real criado a partir do molde.
meu_carro = carro()

#Atributos: São informações que pertencem a um objeto. Podem ser públicos (acessíveis fora da classe) ou privados (usando _ ou __)
class carro:
    def __init__(self, marca, modelo, ano): #método construtor, chamado automaticamente ao criar objeto , usaod para inicializar atributos
        self.marca = marca #Atributo público
        self.__ano = ano #Atributo privado
meu_carro = carro("Toyota", "Corolla", 2022)
print(meu_carro.marca) #Acessível
#print(meu_carro.__ano) #Erro, pois está privado

#Métodos: São funções que pertem a classe e definem comportamentos do objeto
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def apresentar(self): #O self referencia ao proprio objeto (obrigatorio em métodos)
        print(f"Carro: {self.marca}, {self.modelo}")
meu_carro = Carro("Toyota", "Corolla")
meu_carro.apresentar()

#Encapsulamento: Protege dados sensíveis ou criticos dentro da classe usando atributo privados(__atributo).
#Criar getter e setter permite acessar e alterar o atributo de forma controlada:
class ContaBancaria:
    def __init__(self):
        self.__saldo = 100 #privado
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    def ver_saldo(self):
        print(f"Seu saldo atual: {self.__saldo}")
conta = ContaBancaria()
conta.depositar(100)
conta.ver_saldo()

#Herança: Permite criar uma classe filha que herda atributos e métodos da classe pai
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade) #Super -> permite acessar métodos e atributos da classe pai
        self.curso = curso
Aluno1 = Aluno("Samuel", 20, "TI")
print(Aluno1.nome, Aluno1.curso)

#Polimorfismo: O mesmo metodo pode se comportar de formas diferentes em classes diferentes (normalmente em subclasses).
class Animal:
    def falar(self):
        print("Algum som")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

cachorro = Cachorro()
gato = Gato()
cachorro.falar()  # Au au!
gato.falar()      # Miau!
