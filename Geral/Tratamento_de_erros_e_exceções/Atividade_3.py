#Conversor de numeros
try:
    num = int(input("Por favor insira um numero:"))
    resultado = num * 2
except ValueError:
    print("Você não digitou um número válido!")
except Exception as numdec:
    print("Você digitou um número decimal", numdec)
else:
    print(f"O resultado é {resultado}")
finally:
    print("Fim do programa.")