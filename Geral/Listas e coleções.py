#Aula 6 - Listas e Coleções
#listas = [1, 2, 3, 4, 5] - se utiliza para armazenar dados com o list
frutas = ["maças", "banana", "laranja"]
frutas.append("uva") #append para adicionar itens na lista
frutas.remove("banana") #remove para remover itens na lista
print(frutas) #imprime toda a lista
print(frutas[0]) #imprime o primeiro item: maça

#tuple - É uma lista imutável (não pode ser alterada depois de criadas) e criadas com parênteses
cores = ("vermelho", "verde", "azul")
print(cores[1]) # Imprime "verde"

#dict - Coleção de pares chave:valor - muito usado para representar objetos ou dados estruturados e criado com chave {}
pessoa = {
    "nome": "Samuel",
    "idade": 30,
    "cidade": "São Paulo",
    "estudando": True
}
pessoa["altura"] = 1.75  # Adiciona uma nova chave-valor
for chave, valor in pessoa.items():
    print(chave,":",valor)  # Imprime cada chave e seu valor
    
#set - Coleção de valores únicos e não ordenados, criado com chaves {}
numeros = {1, 2, 3, 4, 5, 2, 3, 4} # Duplicados são ignorados
print(numeros)  # Imprime {1, 2, 3, 4, 5} - Duplicados removidos
# Exemplo de uso de set
numeros_unicos = {x for x in range(10) if x % 2 == 0}  # Cria um set com números pares de 0 a 9
print(numeros_unicos)  # Imprime {0, 2, 4

#Atividades sobre a aula 6
#1. Crie uma lista de frutas, adicione mais uma fruta e remova outra

frutas =["Bananas", "Abacaxi", "Morango", "Uva", "Pessêgo"]
frutas.append("Melancia")
frutas.remove("Bananas")
print(frutas)

#2. Crie um dicionário sobre você
Samuel = {
    "nome" : "Samuel",
    "idade" : "24",
    "cidade" : "Barueri",
    "estudando" : True
}
Samuel["altura"] = 1.78
for chave, valor in Samuel.items():
    print(f"{chave}: {valor}")

#. Crie um conjunto com números repetidos
numeros = {1, 2, 3, 4, 5, 2, 3, 4, 1, 5}
print(numeros)