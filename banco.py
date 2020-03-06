print ('Sistema de notas bancárias v1.0')

banco = 0

def menu():
    print ('Escolha uma opção:')
    option = input('1: Deposito \n2: Saque \n3: Saldo \n4: Sair \n \n=>')

    if option == '1':
        print ('\nDeposito selecionado\n')
        deposito()

    elif option == '2':
        print ('\nSaque selecionado\n')
        saque()

    elif option == '3':
        print ('\nSaldo selecionado\n')
        saldoAtual()

    elif option == '4':
        print ('\nSair selecionado\n')
        sair()

    else:
        print ('\nValor inválido. \n Entre um valor válido.')
        menu()

def deposito():
    global banco
    depo = float(input('Valor de deposito: R$'))
    banco = depo + banco
    print ('Foram depositados R${} \nSaldo atual é de R${}'.format(depo, banco))
    enter = input('\nPressione <Enter> para voltar ao Menu de Opções.')

    menu()

def saque():
    global banco
    saq = float(input('Valor do saque: R$'))
    banco = banco - saq
    print ('Foram sacado R${} \nSaldo atual é de R${}'.format(saq, banco))
    enter = input('\nPressione <Enter> para voltar ao Menu de Opções.')

    menu()

def saldoAtual():
    global banco
    print ('\n Seu saldo atual é de R${}'.format(banco))
    enter = input('\nPressione <Enter> para voltar ao Menu de Opções.')

    menu()

def sair():
    print ('Finalizar operações ?')
    print ('\n1: Finalizar \n2: Cancelar')
    option = input('=> ')
    if option == '1':
        exit()

    elif option == '2':
        menu()

    else:
        print ('\nValor inválido. \nEntre um valor válido.')
        sair()


menu()
