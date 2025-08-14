#Desafio 1 - crie uma lista de numero pares
pares = [n for n in range(51) if n %2 == 0] #Pedido de numeros pares até o 50
print(pares)

#Desafio 2 - Nomes Filtrados
nomes = ['ana', 'bruno', 'carla', 'daniel']
nomes_filtro = [nome for nome in nomes if len(nome) >4] #Condição sempre no final e len para pegar o tamanho da palavra
print(nomes_filtro)

#Desafio 3 - Transformação em maiúsculas
frutas = ['maça', 'banana', 'laranja']
frutas_maiusculas = [fruta.upper() for fruta in frutas] #Deixar tudo maiusculo
print(frutas_maiusculas)

#Desafio 4 - Numero ao cubo
cubo = [n**3 for n in range(16)]
print(cubo)

#Desafio 5 - Criando uma lista de tuplas onde cada tupla é (numero, numero ao quadrado)
numeros = [1, 2, 3, 4, 5]
numeros_tupla = [(n, n**2) for n in numeros]
print(numeros_tupla)