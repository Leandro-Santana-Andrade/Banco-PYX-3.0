import os # Adicionado para utilizar a opção de limpar menu
import platform

def menu():

    menu = """ 
                BANCO PYX 2.0
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Usuario
    [5] Cadastrar Conta
    [6] Listar Contas
    [0] Sair

    =>"""
    return int(input(menu))

def depositar(saldo, valor, extrato, /):

    if ( valor > 0 ):
        extrato += (f"Desposito realizado no valor de R$ {valor:.2f}\n")
        saldo += valor    
        limpar()
    else:
        print("Valor invalido, tente novamente!")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):

# Valida se possui saldo ou se esta dentro do limite diario         
    if numero_saques < limite_saques:

        if saque > saldo or limite < saque or saque <= 0:
                    print("Operacao nao permitida, valor insuficiente ou limite diario excedido")
                    print(f"Limite diario R$ {limite}")
                    print(f"Saldo em conta R$ {saldo:.2f}")
        else:
                    saldo = saldo - saque
                    extrato += (f"Saque realizado no valor de R$ {saque:.2f}\n")
                    numero_saques += 1
                    limpar()
    else:
                # Informa que nao ha mais limite para saque e eliminar opção de sacar do menu
                print("Limite de saques excedido")
                menu = """ 
                BANCO PYX
    [1] Depositar
    [3] Extrato
    [0] Sair

    =>"""
    return saldo, extrato

def imprimir_extrato(saldo, *, extrato):
    limpar() 
    if extrato == "":
        print("\n Nao foram realizadas movimentacoes.")
    else:
        print(extrato)
        #print(f"Total de saques realizados: {numero_saques}")        
        print(f"Saldo atual da conta R$ {saldo:.2f}")

    return saldo, extrato

def cadastrar_usuario(usuarios):
     
     limpar() 
     cpf = input("Digite o CPF: ")
     usuario = filtrar_usuario(cpf,usuarios)

     if usuario:
        print("Usuario possui cadastro")

        return
     nome = input("Digite o nome: ")
     dt_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Infome o endereco (logradouro, numero, bairro - cidade/sigla do estado): ")
     usuarios.append({"nome:":nome, "dt_nascimento":dt_nascimento, "cpf": cpf, "endereco": endereco})

     print("Usuario cadastrado!")

def filtrar_usuario(cpf, usuarios):
     
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None 

def cadastrar_conta(agencia, numero_conta, usuarios):

    limpar()  
    cpf = input("Digite o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("Conta criada com sucesso!")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario nao cadastrado!")

def listar_contas (contas):
     
    limpar()  
    if contas == []:
        print("Nenhuma conta cadastrada!")
    else:   
        for conta in contas:
            linha = f"""
    Agencia: {conta['agencia']}
    Conta Corrente: {conta['numero_conta']}
    Titular: {conta['usuario']}
    """
            print("=" * 80)
            print(linha)
            print("=" * 80)

def limpar():

    # Verificar o sistema operacional
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
    
        opcao = menu()

        if opcao == 1: # Opcao de deposito

            valor = float(input("Quanto deseja depósitar? "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2: # Opcao de saque
                
                saque = (float(input("Quanto deseja sacar? ")))

                saldo, extrato = sacar( 
                    saldo=saldo,
                    saque = saque,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=limite_saques,
                )

        elif opcao == 3: # Opção de extrato

            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == 4: # Opção de cadastrar usuario
             
           cadastrar_usuario(usuarios) 
        
        elif opcao == 5: # Opção de cadastrar conta

           numero_conta = len(contas)+1
           conta = cadastrar_conta(agencia, numero_conta, usuarios)  
           
           if conta:
                contas.append(conta)
        
        elif opcao == 6: # Opção de listar conta
             
            listar_contas(contas)

        elif opcao == 0: # Opção de sair da aplicação
            print('''
            Obrigado por utilizar nosso servico!
            ''')
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
