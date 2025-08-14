#1. List Comprehensions — O que é?
#É uma forma compacta e elegante de criar listas a partir de outras iteráveis, aplicando expressões e filtros.
#Exemplo básico:
#Quer criar uma lista com quadrados dos números de 0 a 9.
#Forma tradicional:
quadrados = []
for i in range(10):
    quadrados.append(i**2)
print(quadrados)
#Com list comprehension:
quadrados = [i**2 for i in range(10)]
print(quadrados)
#Exemplo com filtro:
#Quer só os quadrados dos números pares:
pares_quadrados = [i**2 for i in range(10) if i % 2 == 0]
print(pares_quadrados)
#Compreensão em dicionários (dict comprehension):
#Quer criar um dicionário onde a chave é o número e o valor seu quadrado:
quadrados_dict = {i: i**2 for i in range(5)}
print(quadrados_dict)

#Basicamente é a forma mais rapida de criar uma lista em uma unica linha.
#Vantagens:
#Código mais curto e facil de ler(quando simples)
#Menos linhas, menos chance de erro.
#QUANDO EVITAR!
#Se ficar muito complexo e dificil de endenter
#Para lógicas muito longas ou com muitas condições