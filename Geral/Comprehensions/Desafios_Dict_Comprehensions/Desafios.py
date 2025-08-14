# Desafio 1 - Comprimento dos nomes
nomes = ['ana', 'joão', 'bruno', 'daniel']
tamanho_nomes = {nome: len(nome) for nome in nomes} #ele retorna o nome da pessoa : tamanho da palavra
print(tamanho_nomes)

# Desafio 2 - Crie um dicionário com numero de a 1 a 10 como chave e sua raiz quadrada como valor
raiz_numero = {n: n**0.5 for n in range(1, 11)}
print(raiz_numero)

# Desafio 3 - Dicionário invertido
original = {'a': 1, 'b': 2, 'c': 3}
invertido = {valor: chave for chave, valor in original.items()}
print(invertido)

# Desafio - 4 Dicionario de booleanos, dizer se o numero é par ou impar 
lista = [10, 21, 32, 43, 54]
n = {n: n % 2 == 0 for n in lista }
print(n)

# Desafio - 5 dicionário filtrado, crie uma nova lista só com pessoas acima do 30
dados = {'ana':25, 'bruno':32, 'carla':18, 'daniel':40}
lista = {nome:idade for nome, idade in dados.items() if idade >30}
print(lista)