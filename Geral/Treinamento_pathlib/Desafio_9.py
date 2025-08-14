#Desafio 9 - Apagar pasta após confirmação
from pathlib import Path
import shutil
temp_dir = Path("Temp")
if temp_dir.exists() and temp_dir.is_dir():
    print("A pasta já existe")
else:
    print("A pasta não exist")
    temp_dir.mkdir(exist_ok=True)
    print("Pasta criada com sucesso")
dado_arquivo = Path("Dados.txt")
if dado_arquivo.exists() and dado_arquivo.is_file():
    print("O arquvio já existe")
else:
    print("O arquvio não existe")
    dado_arquivo.write_text("Dados temporarios de estudo", encoding="UTF-8")
    print("Arquivo criado com sucesso")
temp_arquivo = Path("Temp.txt")
if temp_arquivo.exists() and temp_arquivo.is_file():
    print("O arquivo já existe")
else:
    print("O arquivo não existe")
    temp_arquivo.write_text("Arquivo temporario de estudo", encoding="UTF-8")
    print("Arquvi criado com sucesso")
shutil.move(dado_arquivo, temp_dir / "Dados.txt")
shutil.move(temp_arquivo, temp_dir / "Temp.txt")
print("Arquivo movido com sucesso")
#Como apagar a pasta por confirmação
apagar = input("Deseja apagar a pasta Temp? (s/n)").strip().lower() #Como confirmar
if apagar == "s":
    if temp_dir.exists() and temp_dir.is_dir():
        shutil.rmtree(temp_dir)
        print("A pasta apagada com sucesso!")
    else:
        print("A pasta Temp não existe para apagar.")
else:
    print("Pasta não apagada")