#Try significa tentar executar o bloco de código mas se der errado pula para except (tipo if e else)
try:
    x = int(input("Digite um número: "))
    print(f"Você digitou {x}")
except ValueError: #Except ele captura um erro específico e serve para tratar o erro
    print("Erro: digite apenas números inteiros!") #Se o usuario tentar digitar letras, vai aparecer a mensagem de erro
else: #Else ele roda somente se o erro não acontecer
    print(f"O dobro é {x*2}")
finally: #Finally sempre executa independente de erro ou não, muito usado para fechar aquivos, conexões, limpar memorias e etc
    print("Fim da execução")

#Raise: Forçar um erro manualmente caso algo não estiver certo
def dividr(a, b):
    if b == 0:
        raise ZeroDivisionError("Você tentou dividir por zero") #Força um erro caso divida por zero já que não tem como
    return a/b
print(dividr(10,2))
print(dividr(10,2)) #forçar o erro #

#Pode usar varios except juntos
try:
    x = int(input("Digite um numero:"))
    resultado = 10 / x
except ValueError:
    print("Erro: Você precisa digitar um nuermo válido")
except ZeroDivisionError:
    print("Erro: Você não pode dividir por zero")
else:
    print(f"O resutado é {resultado}")

#Capturar erro generico: Nem sempre sabemos qual erro pode ocorrer, para capturar um erro génerico:
try:
    x = int("abc")
except Exception as e:
    print("Ocorreu um erro:", e)