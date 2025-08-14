#Desafio 7 - Mover para uma subpasta
from pathlib import Path
import shutil

# Caminho do arquivo
base_financeiro = Path("Financeiro.txt")

# Verificar se o arquivo existe
if base_financeiro.exists():
    print("A base já existe")
else:
    print("A base não existe")
    base_financeiro.write_text("Calculo mensal da empresa", encoding="UTF-8")
    print("Criado com sucesso")
# Pasta de destino
financeiro_dir = Path("Financeiro")
if financeiro_dir.exists() and financeiro_dir.is_dir():
    print("A pasta já existe")
else:
    print("A pasta não existe")
    financeiro_dir.mkdir(exist_ok=True)
    print("Pasta criada com sucesso")

# Mover o arquivo (somente se ela existir)
if base_financeiro.exists():
    shutil.move(base_financeiro, financeiro_dir / "Financeiro.txt")
    print("Arquivo movido para pasta Financeiro com sucesso!")
else:
    print("Não foi possível mover: arquivo não encontrado.")
