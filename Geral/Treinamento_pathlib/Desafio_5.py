#Atividade 5 - Criar um Zip de uma pasta
from pathlib import Path
import shutil
projeto = Path("Projeto")
if projeto.exists() and projeto.is_dir():
    print("A pasta existe :)")
else:
    print("A pasta não existe! :(")
    projeto.mkdir()
    print("A pasta foi criado com sucesso")
arquivo = projeto / "teste.txt"
arquivo.write_text("Linha 1: Testando sobre zipagem\n", encoding="utf-8")
print("Arquivo criado com sucesso!")
shutil.make_archive("teste", "zip", "Projeto") #Compactar arquivo
print("Arquivo compactado com sucesso")
descompactado = Path("Projeto_Descompactado")
descompactado.mkdir(exist_ok=True) #A pasta só é criada se não existir!
print("Pasta criado com sucesso")
shutil.unpack_archive("teste.zip", "Projeto_Descompactado") #Descompactar arquivo
print("Descompactado com sucesso") 