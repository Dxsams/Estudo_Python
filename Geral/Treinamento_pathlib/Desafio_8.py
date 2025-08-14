#Desafio 8 - Criando um backup simples mas com datas
from pathlib import Path
import shutil
#Criar arquivo
dados_arquivo = Path("Dados.txt")
if dados_arquivo.exists() and dados_arquivo.is_file(): #Sempre que for para conferir um arquivo é is_file
    print(f"O arquivo {dados_arquivo} já existe")
else:
    print(f"O arquivo {dados_arquivo} não existe")
    dados_arquivo.write_text("Dados testes", encoding="utf-8")
    print("Arquivo criado com sucesso")
#Criar pasta raiz
contabilidade_dir = Path("Contabilidade")
if contabilidade_dir.exists() and contabilidade_dir.is_dir():
    print(f"A pasta {contabilidade_dir} já existe!")
else:
    print(f"A pasta {contabilidade_dir} não existe")
    contabilidade_dir.mkdir(exist_ok=True)
    print("Pasta criada com sucesso")
#Mover conteudo
shutil.move(dados_arquivo, contabilidade_dir / "Dados.txt")
print("Conteudo criado com sucesso")
#Criar pasta
backups_dir = Path("Backups")
if backups_dir.exists() and backups_dir.is_dir(): #Dempre que for para verificar uma pasta é is_dir
    print(f"A pasta {backups_dir} já existe")
else:
    print(f"A pasta {backups_dir} não existe!")
    backups_dir.mkdir(exist_ok=True)
    print("Pasta criadda com sucesso")
#Mover um conteudo a outra pasta
shutil.copy2(contabilidade_dir / "Dados.txt", backups_dir / "Backup_contabilidade_2025-08-12.txt") #Mover conteudo para outra pasta
print("Backup feito com sucesso")