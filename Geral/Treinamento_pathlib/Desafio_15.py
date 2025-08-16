#Desafio 15 - Controle de estoque
#Adicionar bibliotecas necessarios
from pathlib import Path
import shutil
from datetime import datetime
#Criar pasta principal
Estoque_dir = Path("Estoque")
Estoque_dir.mkdir(exist_ok=True)
print("Pasta criada")
#Criar arquivo
estoque_file = Estoque_dir / "Estoque.txt"
conteudo = (
    "Banana - 13.58\n"
    "Maça - 6.68\n"
    "Perâ - 5.00\n"
    "Uva - 3.84\n"
    "Morango - 12.45\n"
)
estoque_file.write_text(conteudo, encoding="UTF-8")
print(f'arquivo {estoque_file} criado com sucesso')
#Ler arquivo e atualizar
estoque_dict = {}
for linha in estoque_file.read_text(encoding="UTF-8").splitlines():
    nome, preço = linha.split(" - ")
    preço = float(preço)
    estoque_dict[nome] = round(preço * 1.12,2)
print("Dicionario atualizado com sucesso", estoque_dict)
##estoque_dict = {
#nome: round(float(preço) * 1.12, 2)
#for nome, preço in (linha.split(" - ") for linha in estoque_file.read_text(encoding="utf-8").splitlines())}
#Segundo modo
#Salvar aquivo atualizado
estoque_atualizado_file = Estoque_dir / "Estoque_atualizado.txt"
estoque_atualizado_text = '\n'.join(f"{nome} - {preço}"for nome, preço in estoque_dict.items())
estoque_atualizado_file.write_text(estoque_atualizado_text, encoding="utf-8")
print("Arquivo atualizado com sucesso")
#criar pasta de backup
Backup_dir = Path("Backup")
Backup_dir.mkdir(exist_ok=True)
print("Pasta criada com sucesso")
#Realizar backup
data_hora = datetime.now().strftime("%Y_%m_%d_%H%M%S")
Backup_file = Backup_dir / f"Estoque_backup_atualizado_{data_hora}.txt"
shutil.copy2(estoque_file, Backup_file)
print("Backup feito com sucesso:", Backup_file)
print("Processo feito com sucesso")