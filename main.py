menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuário
    [c] Criar conta corrente
    [q] Sair
"""

saldo = 0
numero_saques = 0
extrato = []
usuarios = []
contas = []

def saque(**params):
    if params["numero_saques"] == 3:
            print("Você já fez 3 saques hoje. Tente novamente amanhã.")
        
    print("Entre com o valor que deseja sacar:")
    valor_saque = input()

    try:
        valor_saque = float(valor_saque)
    except:
        print("O valor deve ser um número, separando os centavos por ponto (.).")
    
    if valor_saque < 0:
        valor_saque = abs(valor_saque)

    params["extrato"].append(f"Saque: R$ {valor_saque}")
    params["saldo"] -= valor_saque
    params["numero_saques"] += 1
    params["extrato"].append(f"Saldo: R$ {saldo}")

    return params["extrato"], params["saldo"], params["numero_saques"]


def deposito(param_extrato, param_saldo):

    print("Entre com o valor do depósito:")
    valor = input()

    try:
        valor = float(valor)
    except:
        print("O valor deve ser um número, separando os centavos por ponto (.).")
        
    if valor < 0:
        print("Só valores positivos são aceitos.")

    param_extrato.append(f"Depósito: R$ {valor}")
    param_saldo += valor
    param_extrato.append(f"Saldo: R$ {param_saldo}")

    return param_saldo, param_extrato

def fun_extrato (param_saldo, **param_extrato):
    if not len(param_extrato["extrato"]):
        print("Não foram realizadas movimentações.")

    extrato_list = "\n".join(extrato) +  "\n" + f"Saldo atual: {param_saldo}"

    print(extrato_list)

def criar_usuario():
    novo_usuario = {
        "nome": "",
        "nascimento": "",
        "cpf": "",
        "endereco": ""
    }

    novo_usuario["nome"] = input("Nome completo:")
    novo_usuario["nascimento"] = input("Data de nascimento (DD/MM/AAAA):")
    novo_usuario["cpf"] = input("CPF - Somente números:")

    teste = [x for x in usuarios if x["cpf"] == novo_usuario["cpf"]]

    if len(teste):
        print("Este CPF está associado a outro usuário do sistema.")

    endereco_completo = []
    rua = input("Endereço - Rua:")
    endereco_completo.append(rua)
    endereco_completo.append(", ")
    nro = input("Endereço - Numero:")
    endereco_completo.append(nro)
    endereco_completo.append(" - ")
    bairro = input("Endereço - Bairro:")
    endereco_completo.append(bairro)
    endereco_completo.append(" - ")
    cidade = input("Endereço - Cidade:")
    endereco_completo.append(cidade)
    endereco_completo.append("/")
    estado = input("Endereço - Sigla do Estado:")
    endereco_completo.append(estado)

    novo_usuario["endereco"] = "".join(endereco_completo)

    usuarios.append(novo_usuario)

def criar_conta(contas):
    cpf_usuario = input("Digite o cpf do usário que será dono da conta (somente números): ")

    usuario = [x for x in usuarios if x["cpf"] == cpf_usuario]

    if not len(usuario):
        print("Não existe um usário com este CPF cadastrado no sistema.")

    if len(contas):
        nova_conta = contas[-1]["numero"] + 1
    else:
        nova_conta = 1

    conta_corrente = {
        "Agência": "0001",
        "número": nova_conta,
        "usuário": {
            "nome": usuario[0]["nome"],
            "cpf": usuario[0]["cpf"]
        }
    }

    return contas

    
while True:

    opcao = input(menu)

    if opcao == "d":
        new_extrato, new_saldo = deposito(extrato, saldo)
        extrato = new_extrato
        saldo = new_saldo

    elif opcao == "s":
        params = {
            "saldo": saldo,
            "numero_saques": numero_saques,
            "extrato": extrato,
        }

        new_extrato, new_saldo, new_numero_saques = saque(**params)

        saldo = new_saldo
        numero_saques = new_numero_saques
        extrato = new_extrato
    
    elif opcao == "e":
        param_extrato = {
            "extrato": extrato
        }
    
        fun_extrato(saldo, **param_extrato)

    elif opcao == "u":
        criar_usuario()
    
    elif opcao == "c":
        contas = criar_conta(contas)        

    elif opcao == "q":
        break
    
    else:
        print("Você selecionou uma opção inválida. Por favor seleciona novamente a operação desejada.")