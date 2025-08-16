#Faça um programa que divide por dois numeros e trate possiveis erros
try:
    num1 = int(input("Por favor insira o primeiro numero:"))
    num2 = int(input("Por favor insira o segundo numero:"))
    resultado = num1 / num2
except ValueError:
    print("Por favor não insira letras")
except ZeroDivisionError:
    print("Não foi possivel dividir por zero")
else:
    print(f"O resultado é {resultado}")
finally:
    print("Fim do processo")