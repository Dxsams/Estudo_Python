#Gerenciamento de produtos e backup
from pathlib import Path
import shutil
from datetime import datetime
produtos_dir = Path("Produtos")
produtos_dir.mkdir(exist_ok=True)
print("Pasta criada com sucesso")
produtos_file = produtos_dir / "Produtos.txt"
conteudo = (
    "Banana - 4.50\n"
    "Maça - 2.80\n"
    "Abacaxi - 13.00\n"
    "Morango - 8.92\n"
    "Uva - 7.85\n"    
)
produtos_file.write_text(conteudo, encoding="utf-8")
print("Arquivo criado com sucesso")
#Criar o dicionario e ler arquivo
produtos_dict = {}
for linha in produtos_file.read_text(encoding="utf-8").splitlines(): #Ler arquivo
    nome, preco = linha.split("-")
    preco = float(preco)
    produtos_dict[nome] = round(preco*1.10,2) #aumento de 10$
    print("Dicionário de produtos atualizado:", produtos_dict)
#salvar arquivo atualizado
atualizado_file = produtos_dir / "Produtos_atualizados.txt"
atualizado_text = '\n'.join(f"{nome} - {preco}" for nome, preco in produtos_dict.items())
atualizado_file.write_text(atualizado_text, encoding="utf-8")
print("Arquivo atualizado salvo com sucesso")
#criar pasta de backup
backup_dir = Path("Backup")
backup_dir.mkdir(exist_ok=True)
#Gerar backup com data e hora
data_hora = datetime.now().strftime("%Y_%m_%d_%H%M%S")
backup_file = backup_dir / f"Produtos_backup_{data_hora}.txt"
shutil.copy2(produtos_file, backup_file)
print("Backup feito com sucesso:", backup_file)
