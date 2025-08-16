#Divisão segura em loop
print("=== Divisão segura ===")
while True:
    try:
        entrada1 = input("Digite o primeiro número (ou 'sair' para encerrar): ").lower()
        if entrada1 == "sair":
            print("Programa encerrado")
            break
        num1 = float(entrada1)

        entrada2 = input("Digite o segundo número (ou 'sair' para encerrar): ").lower()
        if entrada2 == "sair":
            print("Programa encerrado")
            break
        num2 = float(entrada2)

        resultado = num1 / num2
    except ValueError:
        print("Erro: digite apenas números válidos!")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"O resultado de {num1} / {num2} é {resultado}")
    finally:
        print("Próxima operação ou digite 'sair' para encerrar.\n")
