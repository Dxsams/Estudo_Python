texto = "Olá, Samuel!"
print(texto[0])
print(texto)
#basico sobre string

#Fatiamento (slicing) - Basicamente pegar um caractere da frase
texto = "Olá, Samuel!"
print(texto[0:4])
print(texto[5:11])
print(texto[:4])
print(texto[4:])

#Métodos
texto = "Olá, Samuel!"
lista = ['Olá,', 'Samuel!']
print(texto.lower()) #deixa as letras todas minuscula
print(texto.upper()) #Deixas as letras todas maiusculas
print(texto.strip()) #remove os espaços no começo e fim
print(texto.replace("Samuel", "amigo")) #Substitui pedaços da string por outro
print(texto.split()) #Divide a string em uma lista, usando a vírgula como separador
print(" ".join(lista)) #Enquanto split divide em lista, join ele junta em uma string.

#exercicios.

#1. Crie uma string com o seu nome e faça ela aparecer em maiscula e minuscula.
texto = "Olá, Samuel! Bem vindo :)"
print(texto.lower())
print(texto.upper())

#2. Crie uma frase e divide ela.
texto = "Estou estudando python e tentando conseguir meu primeiro emprego internacional"
print(texto.split())

#3. Substitua uma palavra por outra.
texto = "Olá, Samuel! Bem vindo :)"
print(texto.replace("Samuel", "Daniel"))

#4. Junte as palavras da frase com o join()
texto = ['Estou', 'estudando', 'python', 'e', 'tentando', 'conseguir', 'meu', 'primeiro', 'emprego', 'internacional']
print(" ".join(texto))