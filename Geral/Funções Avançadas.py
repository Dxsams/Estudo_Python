#1. Parâmetros padrão
#Você pode definir valores padrão para parâmetros. Se a função for chamada sem esse argumento, o valor padrão é usado.
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao("Samuel")  # Olá, Samuel!
saudacao()          # Olá, Visitante!

#args (Argumentos posicionais variáveis) - Permite passar vários argumentos que serão tratados como tupla dentro da função.
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma(1, 2, 3))       # 6
print(soma(4, 5))          # 9
print(soma(10))            # 10

#**kwargs - argumentos nomeados variáveis - Permite passar vários argumentos nomeados que serão tratados como um dicionário.
def imprime_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprime_info(nome="Samuel", idade=24, cidade="Barueri")

#Funções lambda - Funções anônimas e pequenas - São funcões pequenas, sem nome, usadas geralmente para funções simples
multiplica = lambda x, y: x * y
print(multiplica(5, 4))  # 20

lista = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, lista))
print(quadrados)  # [1, 4, 9, 16, 25]

#1. Crie uma função simples
def enviar_email(mensagem, remetente="Sistema Automático"):
    print(f"Remetente: {remetente} | Mensagem: {mensagem}")

enviar_email("Seu pedido foi aprovado!")  
enviar_email("Sua conta vence amanhã", "Financeiro")


#2. Crie uma função para *

def compras(*itens):
    print("Lista de compras:")
    for i, item in enumerate(itens, start=1):
        print(f"{i}. {item}")

compras("arroz", "feijão", "macarrão")

#3. Crie uma função para **
def perfil_usuario(**usuario):
    print("Dados do usuario")
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

perfil_usuario(nome="Samuel", cidade="Barueri", profissão="Programador")

#4. crie uma função lambda
desconto = lambda preco, pct: preco - (preco*pct /100)
print(desconto(100, 20))

#5. Desafio bonus
def pedido(tamanho="média", *coberturas, **detalhes):
    print(f"Pizza tamanho {tamanho}")
    if coberturas:
        print("Coberturas:", ", ".join(coberturas))
    
    for chave, valor in detalhes.items():
        print(f"{chave}: {valor}")

    preco_base = 30  # valor fixo da pizza
    preco_final = lambda preco, qtd: preco + (qtd * 3)
    print(f"Preço final: R${preco_final(preco_base, len(coberturas)):.2f}")

pedido("grande", "bacon", "milho", pagamento="pix", endereco="Rua X")
