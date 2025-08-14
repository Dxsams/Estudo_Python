#manipulação de arquivos
#lendo um arquivo (open, read, close)
# Cria um arquivo de exemplo (só para este teste)
with open("notas.txt", "w") as f:
    f.write("Samuel - 9.5\n")
    f.write("Maria - 8.7\n")
    f.write("João - 7.0\n")
# Agora vamos abrir para ler
arquivo = open("notas.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()
print("Conteúdo do arquivo:")
print(conteudo)
#lendo linha por linha
with open("notas.txt", "r", encoding="utf-8") as f:
    print("Primeira linha:", f.readline().strip())  # strip remove \n
with open("notas.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()
    print("Todas as linhas como lista:", linhas)
#escrevendo em um arquivo (write, append)
# Modo "w" sobrescreve o arquivo
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Iniciando log...\n")
# Modo "a" adiciona no final
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nova linha adicionada.\n")
#Uso do with open - garante que o arquivo será fechado automaticamente
with open("dados.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha de dados.\n")
    f.write("Segunda linha de dados.\n")
#Desafio real:
def adicionar_tarefa(tarefa):
    with open("tarefas.txt", "a", encoding="utf-8") as f:
        f.write(tarefa + "\n")

def listar_tarefas():
    with open("tarefas.txt", "r", encoding="utf-8") as f:
        tarefas = f.readlines()
    print("Tarefas:")
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. {t.strip()}")

# Testando
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer exercícios")
listar_tarefas()
