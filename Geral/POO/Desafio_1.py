# Agenda de contatos com classe
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_contato(self):
        print(f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}")

# Lista de contatos
agenda = []

# Adicionando contatos
contato1 = Contato("Samuel", "11931450136", "samuelrocha@gmail.com")
contato2 = Contato("Ana", "11999999999", "ana@gmail.com")

agenda.append(contato1)
agenda.append(contato2)

# Exibindo todos os contatos
print("📒 Contatos salvos:")
for c in agenda:
    c.exibir_contato()
