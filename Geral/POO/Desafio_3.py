class Livro: #criar class pai
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
    def emprestar_livro(self): #Função para emprestar
        if self.disponivel:
            self.disponivel = False
            return f'Você vai pegar o livro {self.titulo} do autor {self.autor}'
        else:
            return f'O livro {self.titulo} já está emprestado.'
    def devolver_livro(self): #função para devolver
        if not self.disponivel:
            self.disponivel = True
            return f'Você vai devolver o livro {self.titulo} do autor {self.autor}'
        else:
            return f'O livro {self.titulo} já estava disponivel.'

try:
    titulo = input("Qual o titulo do livro?:").strip()
    autor = input("Qual o autor do livro?:").strip()
    disp = input("O livro está disponivel? (s/n):").strip()
    disponivel = disp in ("s", "sim")
    opcao = input("Quer pegar emprestado ou devolver?").strip().lower()
    
    livros = Livro(titulo, autor, disponivel)
    if opcao == "emprestado":
        print(livros.emprestar_livro())
    elif opcao == "devolver":
        print(livros.devolver_livro())
    else:
        print("Opção inválida")
except Exception as e:
    print("Ocorreu um erro", e)