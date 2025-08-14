#Atividade 2 - Criar um backup simples    
from pathlib import Path
import shutil
p = Path("anotações.txt")
p.parent.mkdir(parents=True, exist_ok=True)
with p.open("w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Fazendo a atividade 1\n")
    arquivo.write("Linha 2: Testando um backup simples\n")
    print("Arquivo criado com sucesso\n")
#criar um backup simples com o shutil
backup = Path("backup_anotações.txt")
shutil.copy(p, backup)
print("Backup criado com sucesso!")
