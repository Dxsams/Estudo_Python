nota = 6

if nota >= 7:
    print("Você foi aprovado, parabens!")
elif nota >= 5 and nota < 7:
    print("Você está em recuperação, estude mais!")
else:
    print("Você foi reprovado, estude mais!")
    
print("Fim do programa")
print("Obrigado por participar!")

# Fim do código aula1.py
# Este é um exemplo simples de controle de fluxo em Python
# Este é um exemplo simples de controle de fluxo em Python
# O código verifica a nota do aluno e imprime uma mensagem de acordo com a situação

#Aula 3 - Loops e Repetições
for i in range(1, 11):
    print("Contando", i)

contador = 0
while contador <11:
    print("Contando", contador)
    contador +=1
print("Fim da aula 3")
#Fim da aula 3 de python

#Aula 4 - funções
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Samuel") #O nome que irá aparecer

def mult(a, b):
    return a * b

resultado = mult(10, 2)
print(f"O resultado do calculo é {resultado}")  # Imprime 8
print("Fim do programa")
#Fim da aula 4 de python

#Aula 5 - Input
nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota:"))
def avaliação(nota):
    if nota >=7:
        print(f"Olá {nome} a sua nota é {nota}, você foi aprovado")
    elif nota >=5 and nota <7:
        print(f"Olá {nome} sua nota é {nota}, você está de recuperação")
    else:
        print(f"Olá {nome} a sua nota é {nota}, você foi reprovado")

notafinal = avaliação(nota)
print("Fim do programa")
#Sempre que for numero, colocar o tipo antes do input
#Exemplo de otimização juntando string com numero e aprendendo mais sobre o print em funções
