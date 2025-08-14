#Desafio 1 - Idade e categoria
idades = {'Ana': 25, 'Bruno': 32, 'Carla': 18, 'Daniel': 40}
resultado ={chave: "adulto" if valor >= 18 else "menor" for chave, valor in idades.items() }
print(resultado)

#Desafio 2 - Preços com imposto
produtos = {'banana': 4.5, 'maça': 3.2, 'laranja': 2.8}
resultado = {frutas: round(preço * 1.15,2 ) for frutas, preço in produtos.items()}
print(resultado)

#Desafio 3 - Filtrar numeros pares
dados = {'a':1, 'b':2, 'c':3, 'd':4}
resultado = {chave: valor for chave, valor in dados.items() if valor % 2 == 0}
print(resultado)

#Desafio 4 - inverter dicionário
dados = {'x':10, 'b':2, 'z':30}
resultado = {valor: chave for chave, valor in dados.items()}
print(resultado)

#Desafio 5 - Letras e código ASCII
dados = ['a', 'b', 'c', 'd']
resultado = {chave: ord(chave) for chave in dados}
print(resultado)