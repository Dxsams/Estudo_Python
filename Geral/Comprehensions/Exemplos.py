#Crie uma lista chamada dobro e que tenho o dobrod e numero 1 a 20
dobro = [n*2 for n in range(21)]
print(dobro)
#Criar uma lista com nomes maiusculos
nomes = ['ana', 'bruno', 'carla']
nomes_maiusculo = [nome.upper() for nome in nomes]
print(nomes_maiusculo)
#Criar um dicionario com nomes acima
nomes = ['ana', 'bruno', 'carla']
tamanho_nome = {nome: len(nome) for nome in nomes}
print(tamanho_nome)
