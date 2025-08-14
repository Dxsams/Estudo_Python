#Desafio 10 - Compactar pasta
from pathlib import Path
import shutil
exemplo_dir = Path("Exemplo")
if exemplo_dir.exists() and exemplo_dir.is_dir():
    print("A pasta já existe")
else:
    print("A pasta não existe")
    exemplo_dir.mkdir(exist_ok=True)
    print("Pasta criada com sucesso!")
exemplo_arquivo = Path("Exemplo.txt")
if exemplo_arquivo.exists() and exemplo_arquivo.is_file():
    print("O arquivo já existe!")
else:
    print("O arquivo não existe!")
    exemplo_arquivo.write_text("Linha teste", encoding="UTF-8")
    print("Arquivo criado com sucesso")
shutil.move(exemplo_arquivo, exemplo_dir / "Exemplo.txt") #Mover arquivo
#Compactar pasta
shutil.make_archive("Exemplo", "zip")
print("Pasta compactada com sucesso")
shutil.move("Exemplo.zip", exemplo_dir / "Exemplo.zip" ) #Colocar o arquivo compactado na mesma pasta criada anteriormente