#Modulo 1 - Crie um programa que pergunte idade e calcule quantos meses a pessoa viveu
idade = int(input("Digite sua idade em anos:"))
meses_vividos = idade * 12
dias_vividos = idade * 365
print(f"Você viveu aproximadamente {meses_vividos} meses e aproximadamente {dias_vividos} dias.")

#Modulo 1 - desafio 2
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero:"))
if num1 > num2:
    print(f'O maior numero é {num1}')
elif num2 > num1:
    print(f'O maior numero é {num2}')
else:
    print('Os dois numeros são iguais')

#modulo 2 - atividade 1
numeros = [i for i in range(2, 52, 2)]
print(numeros)

#modulo 2 - atividade 2
while True:
    escolha = input("Digite algo (ou 'sair' para encerrar): ").lower()
    
    if escolha == "sair":
        print("Programa encerrado.")
        break  # encerra o loop
    else:
        print(f"Você digitou: {escolha}")

#modulo 3 - atividade 1
def lista():
    l = [2, 3, 4, 5, 8, 1, 6]
    resultado = [x / 2 for x in l]  # list comprehension para dividir cada elemento
    return resultado  # retorna a lista resultante

resultado = lista()  # chama a função
print(resultado)
import math
def soma():
    num = int(input("Digite o primeiro numero:"))
    num2 = int(input("Digite o segundo numero: "))
    resultado = num + num2
    return resultado
resultado = soma()
print(resultado)

#Modulo 4 - Estrutura de dados
nota = [1,2,3,4,5,6]
resultado = [i / 2 for i in nota]
print(resultado)

#Modulo 5 - Manipulaçaõ de arquivo
from pathlib import Path
nome = input("Digite seu nome:")
nomes = Path("Nomes")
nomes.mkdir(exist_ok=True)
nomes_file = nomes / "Nomes.txt"
conteudo = (nome)
print("Arquivos criado com sucesso")
nomes_file.read_text(encoding="utf-8")
print(conteudo)
