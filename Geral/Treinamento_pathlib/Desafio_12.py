from pathlib import Path
import shutil

# 1. Criar as pastas origem e destino (se não existirem)
origem = Path("origem")
destino = Path("destino")

origem.mkdir(exist_ok=True)
destino.mkdir(exist_ok=True)

for arquivo in origem.iterdir(): #usado para lista tudo dentro da pasta origem
    if arquivo.is_file():  # vamos copiar somente arquivos, não subpastas
        destino_arquivo = destino / arquivo.name
        shutil.copy2(arquivo, destino_arquivo)  # copy2 mantém metadata
        print(f"Arquivo {arquivo.name} copiado para {destino}")

print("Sincronização concluída!")
