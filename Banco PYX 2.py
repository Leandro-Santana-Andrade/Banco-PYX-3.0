#import os # Adicionado para utilizar a opção de limpar menu
#import platform

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
         transacao.registrar(conta)

    def adicionar_conta(self, conta):
         self.conta.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
         super().__init__(endereco)
         self.nome = nome
         self.data_nascimento = data_nascimento
         self.cpf=  cpf

class Conta:
     def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

@classmethod
def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

@property
def saldo (self):
     return self._saldo

@property
def numero(self):
     return self._numero

@property
def agencia(self):
     return self._agencia

@property
def agencia(self):
     return self._cliente

@property
def historico(self):
    return self._historico

def sacar(self, saque):
    saldo = self.saldo
    excedeu_saldo = saque > saldo

    if excedeu_saldo:
        print("Saldo insuficiente para saque.")
    
    elif saque > 0:
        self._saldo -= saque
        print("Saque realizado com sucesso!")
        return True
    
    else:
        print("Falha na operacao!")
    
    return False    

def depositar(self, deposito):

    if ( deposito > 0 ):
        self._saldo += deposito
        print("Deposito realizado!")
    
    else:
        print("Valor invalido, tente novamente!")
        return False

    return True

class ContaCorrete(Conta):
    pass

class Historico:
    pass

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass


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
