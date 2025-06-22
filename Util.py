import os


def LimparTela():
    os.system('cls')


def Linha(tam = 60):
    return '-' * tam


def Cabecalho(txt):
    print(Linha())
    print(txt.center(60))
    print(Linha())
    

def lerOpcao(lim_sup):
    while True:
        try:
            op = int(input('Digite um numero: '))
            if op >= 0 and op <= lim_sup:
                return op
            else:
                print('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m') 
        except(ValueError, IndexError):
            print('\033[31mVoce nao digitou um numero, tente novamente com um NUMERO INTEIRO \033[m')
            
        