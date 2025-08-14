#Desafio 1 - Quadrados de números pares
quadrado = [n**2 for n in range(1, 21)if n % 2 ==0 ] #Ou fazer in range(2, 21, 2) para numeros pares sem precisar do if
print(quadrado)

#Desafio 2 - Filtrar palavras curtas
nomes = ['daniela', 'bruno', 'sara', 'samuel', 'geovana', 'ana', 'marcos']
filtro = [nome for nome in nomes if len(nome) <= 4 ] #Filtar por quantidade de caracteres
print(filtro)

#Desafio 3 - Multiplicar valores
valores = [1, 3, 5, 7]
resultado = [n*10 for n in valores]
print(resultado)

#Desafio 4 - Crie uma lista com letas maiúsculas de uma frase (ignorando espaços)
frase = "Python é DivertidO" #Nesse caso não transformar em uma lista com []
resultado = [letra.upper() for letra in frase if letra !=" "]
print(resultado)

#Desafio 5 - Lista de tuplas (n,n²)
numero = [(n, n**2) for n in range(1, 11)]
print(numero)