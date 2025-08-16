from pathlib import Path

try:
    # Criando a pasta "Teste" se não existir
    teste_dir = Path("Teste")
    teste_dir.mkdir(exist_ok=True)

    # Definindo o caminho do arquivo dentro da pasta
    teste_file = teste_dir / "Teste.txt"

    # Verificando se o arquivo já existe
    if teste_file.exists() and teste_file.is_file():
        conteudo = teste_file.read_text(encoding="utf-8")
        print("Arquivo já existe. Conteúdo atual:")
        print(conteudo)
    else:
        print("Arquivo não existe. Criando...")
        teste_file.write_text("Teste da linha 1", encoding="utf-8")
        print("Arquivo criado com sucesso!")

except Exception as e:
    print("Ocorreu um erro inesperado:", e)

finally:
    print("Fim da execução")
