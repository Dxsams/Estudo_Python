# ===== Criar ou sobrescrever o arquivo =====
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Este é um teste de escrita.\n")

print("✅ Arquivo criado/atualizado com sucesso.\n")

# ===== Acrescentar novas linhas =====
with open("dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Linha 3: Nova informação adicionada.\n")
    arquivo.write("Linha 4: Outra linha extra.\n")

print("✅ Novas linhas adicionadas.\n")

# ===== Ler e exibir o conteúdo =====
try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("📄 Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("❌ Arquivo não encontrado. Execute a parte de escrita primeiro.")
