def calculadora():
    while True:
        try:
            num1_input = input("Digite o primeiro número (ou 'sair' para encerrar): ").lower()
            if num1_input == "sair":
                print("Fim do programa")
                break
            num1 = float(num1_input)

            num2_input = input("Digite o segundo número (ou 'sair' para encerrar): ").lower()
            if num2_input == "sair":
                print("Fim do programa")
                break
            num2 = float(num2_input)

            print("Escolha a operação:")
            print("1 - Adição (+)")
            print("2 - Subtração (-)")
            print("3 - Multiplicação (*)")
            print("4 - Divisão (/)")
            opcao = input("Digite o número da operação desejada: ")

            if opcao == "1":
                resultado = num1 + num2
            elif opcao == "2":
                resultado = num1 - num2
            elif opcao == "3":
                resultado = num1 * num2
            elif opcao == "4":
                resultado = num1 / num2
            else:
                print("Opção inválida!")
                continue

            print(f"O resultado do cálculo é {resultado}")

        except ValueError:
            print("Erro: digite apenas números válidos!")
        except ZeroDivisionError:
            print("Erro: não é possível dividir por zero!")
        finally:
            print("Operação finalizada\n")

calculadora()
 