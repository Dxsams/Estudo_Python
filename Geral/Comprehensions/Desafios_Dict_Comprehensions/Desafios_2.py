#Desafio 1 - Quadrados em dicionário
quadrado = {n: n**2 for n in range(1, 6)}
print(quadrado)

#Desafio 2 - Mapeamento de letras e códigos ASCII
palavra = "Python"
ascii_map = {letra: ord(letra) for letra in palavra}
print(ascii_map)
#letra: ord(letra) cria um par chave:valor, onde a chave é a letra e o valor é o código ASCII da letra
#ord() é a função que retorna o código de um caractere.

#Desafio 3 - Filtar dicionário por valor
idade = {'Ana':25, 'Bruno': 32, 'Carla': 18, 'Daniel': 40}
resultado = {chave: valor for chave, valor in idade.items() if valor < 30} #Para pegar a chave e o valor usa .items()
print(resultado)

#Desafio 4 - Transformar valores
precos = {'banana': 4.5, 'maça': 3.2, 'laranja': 2.8}
resultado = {fruta: round(preço * 1.10, 2) for fruta, preço in precos.items()} #round para decimais 
print(resultado)

#Desafio 5 - Inverter chave e valor
dado = {'a':1, "b":2, "c":3}
resultado = {valor: chave for chave, valor in dado.items()}
print(resultado)