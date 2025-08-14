#Atividade 1 - Verificar se pasta existe
from pathlib import Path
pasta = Path("Desafio_1")
if pasta.exists() and pasta.is_dir(): #.is_dir é garantir que é uma pasta e não arquivo
    print("A pasta existe")
else:
    print("A pasta não existe")
    pasta.mkdir()#criar uma pasta caso não exista
    print("Pasta criada")
