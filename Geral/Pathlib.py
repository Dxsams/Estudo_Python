#Conceito basico de Pathlib
#antes usava-se o modulo os para manipular arquivos, mas agora usa-se o Pathlib
from pathlib import Path

caminho = Path("pasta") / "subpasta" / "arquivo.txt"
print(caminho)

#Principais usos do Pathlib
#1. Manipulação de caminhos de forma intuitiva
#2. Verificação de existência de arquivos e diretórios
#3. Leitura e escrita de arquivos de forma simplificada
#4. Navegação em diretórios
#5. Suporte a operações de sistema de arquivos de forma multiplataforma

# ====== Manipulação de arquivos com Pathlib ======
#1. criar um arquivo
from pathlib import Path
p = Path("dados.txt")  # Cria um objeto Path para o arquivo
p.parent.mkdir(parents=True, exist_ok=True)  # Garante que o diretório pai exista
with p.open("w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Este é um teste de escrita.\n")
    print("✅ Arquivo criado e escrito com sucesso.\n")
#2. verificar se o arquivo existe
from pathlib import Path
p = Path("dados.txt")
if p.exists():
    print("📁 O arquivo existe.")
else:
    print("❌ O arquivo não existe.")
#3. criar pasta
from pathlib import Path # Cria um objeto Path para a nova pasta
pasta = Path("nova_pasta") # Garante que a pasta seja criada
pasta.mkdir(parents=True, exist_ok=True) # Garante que a pasta seja criada
print("✅ Pasta criada com sucesso.") # Cria uma nova pasta
#4. ler e escrever arquivos
from pathlib import Path
p = Path("texto.txt") # Cria um objeto Path para o arquivo
p.write_text("Este é um exemplo de texto.\n", encoding="utf-8") # Escreve o texto no arquivo
conteudo = p.read_text(encoding="utf-8") # Lê o conteúdo do arquivo
print("📄 Conteúdo do arquivo:")
print(conteudo)
#5. listar arquivos em um diretório
from pathlib import Path
diretorio = Path(".")  # Diretório atual
for arquivo in diretorio.iterdir():
    print(arquivo.name)
#6. filtrar por tipo de arquivo
from pathlib import Path
diretorio = Path(".")  # Diretório atual
for arquivo in diretorio.glob("*.txt"):  # Filtra apenas arquivos .txt
    print("📄 Arquivo encontrado:", arquivo.name)
#7. Informações sobre o arquivo
from pathlib import Path
p = Path("dados.txt")
print("📄 Informações sobre o arquivo:")
print("Nome:", p.name)
print("Caminho:", p.resolve())
print("Tamanho:", p.stat().st_size, "bytes")
print("Extensão:", p.suffix)
print("Pasta:", p.parent)
#8. Verificar se a pasta existe
from pathlib import Path
pasta = Path("nova_past")
if pasta.exists() and pasta.is_dir():
    print("✅ A pasta existe.")
else:
    print("❌ A pasta não existe.")
