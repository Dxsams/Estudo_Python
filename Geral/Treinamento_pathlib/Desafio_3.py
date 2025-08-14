#Atividade 3 - Mover arquivos por extensão
from pathlib import Path
import shutil
pasta_origem = Path("arquivos")
pasta_destino = Path("texto")
pasta_destino.mkdir(exist_ok=True)
print("Pasta criado com sucesso")
for arquivo in pasta_origem.glob("*.txt"):
    if arquivo.is_file():
        shutil.move(str(arquivo), pasta_destino / arquivo.name)
        print(f"Arquivo {arquivo.name} movido com sucesso!")
