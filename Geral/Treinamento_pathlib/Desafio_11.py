from pathlib import Path
import shutil
compactados_dir = Path("Compactados")
if compactados_dir.exists() and compactados_dir.is_dir():
    print("Pasta já existe")
else:
    print("Pasta não existe")
    compactados_dir.mkdir(exist_ok=True)
    print("Pasta criada com sucesso")
dados_arquivo = Path("Dados.txt")
if dados_arquivo.exists() and dados_arquivo.is_file():
    print("Arquivo já criado anteriormente")
else:
    print("Arquivo ainda não criado")
    dados_arquivo.write_text("Teste para compactação e descompactação", encoding="UTF-8")
    print("Arquivo criado com sucesso")
#Compactar e movimentar o arquivo
shutil.make_archive("Dados", "zip")
print("Compactado e arquivado com sucesso!")
shutil.move("Dados.zip", compactados_dir / "Dados.zip")
print("Movido com sucesso")
#Criar nova pasta para receber o arquivo
descompactados_dir = Path("Descompactados")
if descompactados_dir.exists() and descompactados_dir.is_dir():
    print("Pasta já criada")
else:
    print("Pasta ainda não criada!")
    descompactados_dir.mkdir(exist_ok=True)
    print("Pasta criada com sucesso!")
#Descompactar arquivo
shutil.unpack_archive(compactados_dir / "Dados.zip", descompactados_dir) 
print("Arquivo movido e descompactado com sucesso!")