from pathlib import Path
import shutil
import random #Importar para utilziar o random
lista = [random.randint(1,200) for _ in range(25)] #Lista random
pares = [i for i in lista if i % 2 == 0 ] #Lista de pares
quadrados ={n**2 for n in pares} #Dict de numero quadrados de pares
Dados_dir = Path("Dados")
Relatorios_dir = Path("Relatorios")
Backup_dir = Path("Backup")
for pasta in [Dados_dir, Relatorios_dir, Backup_dir]: #Criar pastas
    pasta.mkdir(exist_ok=True)
    print("Pastas criado com sucesso")
relatorio = Relatorios_dir / "relatorio.txt" #Criar o arquivo
conteudo = (
    f"lista original: {lista}\n"
    f"pares: {pares} \n"
    f"dicionario: {quadrados} \n"
) 
relatorio.write_text(conteudo, encoding="utf-8") #Conteudo do arquivo
print("Arquivo criado com sucesso")
novo = Dados_dir / "relatorio.txt" #Pegar o arquivo da pasta origem
shutil.move(relatorio, novo) 
shutil.copy(novo, Backup_dir / "Relatorio_backup.txt")
print("Relatorio gerado e movido com sucesso")