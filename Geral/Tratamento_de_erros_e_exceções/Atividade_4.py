from pathlib import Path

# Nome do arquivo
nome_arquivo = input("Digite o nome do arquivo (ex: teste.txt): ")

# Criar pasta para armazenar o arquivo
pasta = Path("Arquivos")
pasta.mkdir(exist_ok=True)

caminho_arquivo = pasta / nome_arquivo

try:
    # Tenta ler o arquivo
    conteudo = caminho_arquivo.read_text(encoding="utf-8")
    print("Arquivo já existe. Conteúdo:")
    print(conteudo)

except FileNotFoundError:
    # Se não existir, cria o arquivo
    print("Arquivo não encontrado. Criando arquivo...")
    caminho_arquivo.write_text("Conteúdo inicial do arquivo", encoding="utf-8")
    print("Arquivo criado com sucesso!")

except Exception as e:
    # Captura outros erros inesperados
    print("Ocorreu um erro inesperado:", e)

finally:
    print("Fim da execução")
