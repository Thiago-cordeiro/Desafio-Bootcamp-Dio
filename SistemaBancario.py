menu = """

[1]depositar
[2]saque
[3]extrato
[0]sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    
    global saldo
    global extrato
    saldo += valor
    extrato.append(f"Depósito: +R$ {valor:.2f}")



def validarSaque(valor):

    global numero_saques
    global LIMITE_SAQUES

    if valor > 500:
        print("\nSaque Maior Que o Permitido".center(30, "-"))

    elif numero_saques >= LIMITE_SAQUES:
        
        print("\nNumero limite de saques atingido".center(30, "-"))

    else:
        numero_saques = numero_saques + 1
        saque(valor)
        
        
def saque(valor):
    global saldo
    global extrato

    if saldo <= 0:
        print("\n Saldo Insuficiente".center(30, "-"))
    elif valor > saldo:
        print("\n Saldo Insuficiente".center(30, "-"))
    else:    
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")

def mostrar_extrato():
    print("\n EXTRATO".center(30, "-"))
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("-" * 30)

while(True):

    opcao = int(input(menu))

    if opcao == 0:
        break
    
    elif opcao == 1:
        
        print("====================================================================")
        print("Selecionado Depósito")
        print("====================================================================")
        inputDeposito = float(input("QTDE a Depositar: "))
        deposito(inputDeposito)
    
    elif opcao == 2:
        
        print("====================================================================")
        print("Selecionado Saque")
        print("====================================================================")

        inputSaque = float(input("QTDE a Sacar: "))
        validarSaque(inputSaque)
        
    
    elif opcao == 3:
        mostrar_extrato()
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")