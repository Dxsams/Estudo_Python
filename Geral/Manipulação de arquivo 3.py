#Modos de abrir arquivos
#Quando você usa open("arquivo", modo, =...), o modo determina o que você pode fazer:
#"r" — ler (padrão). Erro se o arquivo não existir (FileNotFoundError).
#"w" — escrever, sobrescreve o arquivo se existir (cria se não existir).
#"a" — anexar (append): escreve no final, cria se não existir.
#"x" — criar exclusivamente: erro se o arquivo já existir.
#"r+" — ler e escrever (não apaga o conteúdo existente).
#Acrescente "b" para modo binário (ex: "rb", "wb"), usado para imagens/arquivos não-texto.
#Acrescente "t" para modo texto (padrão) — encoding relevante.
#with — o jeito recomendado (context manager)
#Usar with open(...) as f: garante que o arquivo será fechado automaticamente.

#Exemplo completo:# ===== Criar ou sobrescrever o arquivo =====
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Este é um teste de escrita.\n")
print("✅ Arquivo criado/atualizado com sucesso.\n")

#leitura do arquivo
#1. ler tudo de uma vez - read(). utilizado para arquivos pequenos
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("📄 Conteúdo do arquivo:")
    print(conteudo)
#2. ler linha por linha - readline()
with open("dados.txt", "r", encoding="utf-8") as f:
    primeira = f.readline()
    segunda = f.readline()
    print("📄 Primeira linha:", primeira.strip())  # strip remove \n
    print("📄 Segunda linha:", segunda.strip())
#3. ler todas as linhas como lista - readlines() - cada item tem o \n no final. Usar strip() para remover isso se necessário
with open("dados.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()
    print("📄 Todas as linhas como lista:", [linha.strip() for linha in linhas])
#4. iterar sobre o arquivo linha a linha (mais eficiente para arquivos grandes)
with open("dados.txt", "r", encoding="utf-8") as f:
    print("📄 Iterando sobre o arquivo linha a linha:")
    for linha in f:
        print(linha.strip())
#5. Ler em blocos(chunks) - útil para arquivos grandes
def ler_em_blocos(nome_arquivo, tamanho_bloco=1024):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        while True:
            bloco = f.read(tamanho_bloco)
            if not bloco:
                break
            print("📄 Bloco lido:", bloco.strip())
ler_em_blocos("dados.txt", tamanho_bloco=20)
# ======= Escrever no arquivo =======
#1. escrever no arquivo - write() - sobrescreve o conteúdo existente
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 3: Adicionando mais uma linha.\n")
    print("✅ Conteúdo sobrescrito com sucesso.\n") 
#2. adicionar ao final do arquivo - append() - não sobrescreve, adiciona ao final
with open("dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Linha 4: Adicionando mais uma linha ao final.\n")
    print("✅ Conteúdo adicionado com sucesso.\n")
#3. escrever várias linhas - writelines() - aceita uma lista de strings
with open("dados.txt", "a", encoding="utf-8") as arquivo:
    linhas_para_adicionar = ["Linha 5: Outra linha.\n", "Linha 6: E mais uma.\n"]
    arquivo.writelines(linhas_para_adicionar)
    print("✅ Várias linhas adicionadas com sucesso.\n")
#4. escrever em flush - flush() - força a escrita no disco, útil em casos específicos
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 7: Escrevendo e forçando flush.\n")
    arquivo.flush()  # Garante que o conteúdo seja escrito imediatamente
    print("✅ Flush realizado com sucesso.\n")
#5. seek - seek() - reposiciona o cursor de leitura/escrita
with open("dados.txt", "r+", encoding="utf-8") as arquivo:  
    arquivo.seek(0)  # Volta para o início do arquivo
    conteudo = arquivo.read()
    print("📄 Conteúdo após seek:", conteudo.strip())
    arquivo.write("\nLinha 8: Adicionando após seek.\n")
    print("✅ Linha adicionada após seek com sucesso.\n")
#6. tell - tell() - mostra a posição atual do cursor
with open("dados.txt", "r+", encoding="utf-8") as arquivo:
    posicao_inicial = arquivo.tell()  # Posição inicial do cursor
    print("📍 Posição inicial do cursor:", posicao_inicial)
    conteudo = arquivo.read()
    posicao_final = arquivo.tell()  # Posição após ler o conteúdo
    print("📄 Conteúdo lido:", conteudo.strip())
    print("📍 Posição final do cursor:", posicao_final)
    arquivo.seek(posicao_inicial)  # Retorna para a posição inicial
    arquivo.write("\nLinha 9: Adicionando após tell.\n")
    print("✅ Linha adicionada após tell com sucesso.\n")
# ====== pathlib ======
#1. os e pathlib - manipulação de caminhos de arquivos
from pathlib import Path #importando a biblioteca pathlib
p = Path("dados.txt")  # Cria um objeto Path para o arquivo
p.parent.mkdir(parents=True, exist_ok=True)  # Garante que o diretório pai exista
with p.open("w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 10: Usando pathlib para escrever.\n")
    print("✅ Arquivo criado com pathlib com sucesso.\n") # Usando pathlib
# ====== erros comuns ======
#1. FileNotFoundError - arquivo não encontrado
#2. PermissionError - sem permissão para acessar o arquivo
#3. IsADirectoryError - tentando abrir um diretório como arquivo
#4. IOError - erro de entrada/saída, geralmente relacionado a problemas de leitura/escrita
#5. ValueError - erro de valor, geralmente relacionado a modos de abertura inválidos
#6. UnicodeDecodeError - erro ao decodificar texto, geralmente relacionado a problemas de codificação
# ====== Boas práticas ======
#1. Sempre use o modo "with" para garantir que o arquivo seja fechado corretamente.
#2. Use encoding adequado (ex: "utf-8") para evitar problemas de codificação.
#3. Sempre trate exceções ao trabalhar com arquivos para evitar falhas inesperadas.
#4. Use pathlib para manipulação de caminhos de arquivos, pois é mais robusto e fácil de usar.
#5. Sempre verifique se o arquivo existe antes de tentar ler ou escrever nele.
#6. Use funções como os.path.exists() para verificar a existência do arquivo.
#7. Mantenha o código limpo e organizado, separando as operações de leitura e escrita em funções quando necessário.
#8. Documente o código para facilitar a compreensão e manutenção futura.
#9. Use comentários para explicar partes complexas do código.
#10. Não carregue arquivos grandes na memória de uma só vez; use leitura em blocos ou linha a linha.
#11. Sempre faça backup de arquivos importantes antes de realizar operações de escrita.
#12. Valide entradas do usuário ao trabalhar com arquivos, especialmente se o caminho do arquivo for fornecido por ele.
#13. Escrita atômica: sempre verifique se o arquivo foi escrito corretamente, especialmente em operações críticas.

# ====== Exemplo de manipulação de arquivos com pathlib ======
from pathlib import Path

ARQUIVO = Path("tarefas.txt")

def adicionar_tarefa(tarefa):
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    with ARQUIVO.open("a", encoding="utf-8") as f:
        f.write(tarefa.strip() + "\n")

def listar_tarefas():
    if not ARQUIVO.exists():
        print("Nenhuma tarefa ainda.")
        return
    with ARQUIVO.open("r", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            print(f"{i}. {linha.strip()}")

def remover_tarefa(indice):
    if not ARQUIVO.exists():
        print("Arquivo não existe.")
        return
    with ARQUIVO.open("r", encoding="utf-8") as f:
        linhas = f.readlines()
    try:
        linhas.pop(indice - 1)
    except IndexError:
        print("Índice inválido.")
        return
    # sobrescreve de forma segura
    with ARQUIVO.open("w", encoding="utf-8") as f:
        f.writelines(linhas)

# Teste rápido
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer exercícios")
listar_tarefas()
remover_tarefa(1)
listar_tarefas()
