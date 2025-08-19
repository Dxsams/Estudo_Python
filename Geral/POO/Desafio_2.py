#Sitema de alunos - Crie uma classe Aluno e adicone metodos de aprovação
class Alunos:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas #Lista de nots do aluno
        
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"{self.nome} foi Aprovado com média {media:.2f}"
        else:
            return f"{self.nome} foi Reprovado com média {media:.2f}"
        
try:
    nome = input("Digite o nome do aluno:")
    matricula = input("Digite a matricula do aluno:")
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    aluno = Alunos(nome, matricula, [nota1, nota2])
    print(aluno.verificar_aprovacao())
except ValueError:
    print("Por favor, insira apenas números nas notas.")
except Exception as e:
    print("Aconteceu um erro", e)
