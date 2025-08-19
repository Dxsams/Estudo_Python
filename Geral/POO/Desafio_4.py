class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self): # "Como quero que o meu objeto apareça como texto."
        return f"{self.nome} - R${self.preco:.2f} (x{self.quantidade})"


class Carrinho:
    def __init__(self):
        self.produtos = []  # lista de produtos

    def adicionar_produto(self, produto):
        if produto.quantidade > 0:
            self.produtos.append(produto)
            print(f"✅ {produto.quantidade}x {produto.nome} adicionado(s) ao carrinho.")
        else:
            print("⚠️ Quantidade inválida para adicionar.")

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                print(f"🗑️ Produto {nome} removido do carrinho.")
                return
        print("⚠️ Produto não encontrado no carrinho.")

    def exibir(self):
        if not self.produtos:
            print("🛒 Seu carrinho está vazio.")
        else:
            print("🛍️ Produtos no carrinho:")
            total = 0
            for produto in self.produtos:
                print(f"- {produto}")
                total += produto.preco * produto.quantidade
            print(f"💰 Total da compra: R${total:.2f}")


# -------------------------
# Testando o carrinho
carrinho = Carrinho()

# Criando produtos
p1 = Produto("Camisa", 50.0, 2)
p2 = Produto("Tênis", 200.0, 1)

# Adicionando
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)

# Exibindo
carrinho.exibir()

# Removendo
carrinho.remover_produto("Camisa")

# Exibindo de novo
carrinho.exibir()
