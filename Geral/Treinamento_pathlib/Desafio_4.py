#Atividade 4 - Apagar pastas
from pathlib import Path
import shutil
teste = Path("Pasta_Teste")
if teste.exists() and teste.is_dir():
    print("A pasta existe")
else:
    print("A pasta não existe")
    teste.mkdir()
    print("A pasta foi criada com sucesso!")
arquivo = teste / "test.txt"
arquivo.write_text("Linha 1: Teste\n", encoding="utf-8") #Quando for apenas texto simples assim
with open(arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 2: Outro modo de escrever dentro da pasta\n") #Quando for algo mais complexo (projetos grandes)
print("Arquivo criado com sucesso dentro da pasta\n")
shutil.rmtree(teste) #Excluir pasta (CUIDADO!! EXCLUI TUDO DE UMA VEZ)
print("Pasta excluida com sucesso!")
