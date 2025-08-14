#Desafio 1 - Números ímpares ao quadrado
quadrado = [n**2 for n in range(1, 21) if n %2 !=0]
print(quadrado)

#Desafio 2 - Lista de letras de uma frase sem espaços
frase = "Python é divertido"
resultado = [letra.upper() for letra in frase if letra !=" "]
print(resultado)

#Desafio 3 - Multiplicação condicional 
resultado = [n*2 for n in range(1, 16) if n %2==0]
print(resultado)

#Desafio 4 - Tuplas (n,n³)
resultado = [(n, n**3) for n in range(1, 11)]
print(resultado)

#Desafio 5 - Filtrando palavras
palavras = ['casa', 'carro', 'bicicleta', 'avião', 'ônibus']
resultado = [i for i in palavras if len(i) > 5]
print(resultado)