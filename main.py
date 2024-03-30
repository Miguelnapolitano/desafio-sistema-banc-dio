menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
numero_saques = 0
extrato = []

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Entre com o valor do depósito:")
        valor = input()

        try:
            valor = float(valor)
        except:
            print("O valor deve ser um número, separando os centavos por ponto (.).")
            continue
            
        if valor < 0:
            print("Só valores positivos são aceitos.")
            continue

        extrato.append(f"Depósito: R$ {valor}")
        saldo += valor
        extrato.append(f"Saldo: R$ {saldo}")


    elif opcao == "s":
        if numero_saques == 3:
            print("Você já fez 3 saques hoje. Tente novamente amanhã.")
        
        print("Entre com o valor que deseja sacar:")
        valor_saque = input()

        try:
            valor_saque = float(valor_saque)
        except:
            print("O valor deve ser um número, separando os centavos por ponto (.).")
            continue
        
        if valor_saque < 0:
            valor_saque = abs(valor_saque)

        extrato.append(f"Saque: R$ {valor_saque}")
        saldo -= valor_saque
        numero_saques += 1
        extrato.append(f"Saldo: R$ {saldo}")
    
    elif opcao == "e":
        if not len(extrato):
            print("Não foram realizadas movimentações.")

        extrato_list = "\n".join(extrato)

        print(extrato_list)
    
    elif opcao == "q":
        break
    
    else:
        print("Você selecionou uma opção inválida. Por favor seleciona novamente a operação desejada.")