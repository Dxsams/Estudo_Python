#Cópia Simples com verificação
from pathlib import Path
import shutil
relatorio_dir = Path("Relatorio")
if relatorio_dir.exists() and relatorio_dir.is_dir(): #Confirmar que é uma pasta e não um arquivo
    print("A pasta existe")
else:
    print("A pasta não existe!")
    relatorio_dir.mkdir(exist_ok=True) #Criar pasta caso não exista
    print("A pasta foi criada com sucesso")
relatorio_arquivo = relatorio_dir / "Relatorio.txt"
relatorio_arquivo.write_text("Fazendo testes", encoding="utf-8") #Criando o arquivo
print("Arquivo criado com sucesso!") #Confirmação que foi criado
backup_dir = Path("Relatorio_backup")
backup_dir.mkdir(exist_ok=True) #Criar a pasta de backup
if relatorio_arquivo.exists(): #Garanta que o arquivo exista antes de fazer backup
    shutil.copy(relatorio_arquivo, backup_dir / "Relatorio.txt") #Caminho que vai ser copiado e realizando backup
    print("Backup feito com sucesso")
else:
    print("O arquivo original não existe, não foi possivel completar")
    