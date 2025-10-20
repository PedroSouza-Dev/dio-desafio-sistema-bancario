"""
Crie um programa que simule um sistema bancário simples, permitindo ao usuário:

Depositar valores (somando ao saldo e registrando no extrato);

Sacar valores (limitado a R$500 por saque e 3 saques diários);

Visualizar o extrato (mostrando depósitos, saques e saldo atual);

Sair do programa ao digitar [q].

Use um menu interativo com as opções [d] Depositar, [s] Sacar, [e] Extrato e [q] Sair.
Valide as operações e exiba mensagens de erro quando o valor for inválido ou as regras forem violadas.

"""

# 1a etapa: fazer a operacao normal
"""
    1. Operação para cheque especial: saque só pode ser maior que o saldo se a pessoa tiver cheque especial
    configurar o limite de cheque especial


"""
# 2a etapa: fazer as validacoes de dados com try e except

from datetime import datetime
import time

# fazer do jeito que eu faria se eu não soubesse 

saldo = 0
deposito = 0
extrato = ""
LIMITE_EXTRATO = 3
LIMITE_SAQUE = 500

enunciado = """

===========================

    ESCOLHA A OPÇÃO:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

===========================

:

"""

while True:

    opcao = str(input(enunciado))
    op = opcao.lower()

    # configuracoes de tempo
    year_current = datetime.now().year 
    month_current = datetime.now().month
    day_current = datetime.now().day
    now = datetime.now().time()
    format_time = now.strftime("%H:%M:%S") #GPT

    # Depositar
    if op == "d":
        deposito_valor = float(input("Digite o valor que você deseja depositar: "))
        saldo += deposito_valor
        extrato += f"\n +{deposito_valor} - {day_current}/{month_current}/{year_current} - {format_time} \n Saldo Atual: {saldo: .2f}"
        print("Deposito feito com sucesso!")
    
    #Sacar
    elif op == "s":
        saque_valor = float(input("Digite o valor que você deseja sacar: "))
        saldo -= saque_valor
        extrato += f"\n -{saque_valor} - {day_current}/{month_current}/{year_current} - {format_time} \n Saldo Atual: {saldo: .2f}"
        print("Sacando o valor de {:.2f}".format(saque_valor))

    #Extrato: historico da conta depositos e saques
    elif op == "e":
        extrato_final = f"""

                EXTRATO DE TRANSAÇÕES ATÉ {day_current}/{month_current}/{year_current} | {format_time}

                {extrato}

                VALOR EM CONTA: {saldo: .2f}

        """
        print(extrato_final)

    #Sair
    elif op == "q":
        print("Operação encerrada!")
        break