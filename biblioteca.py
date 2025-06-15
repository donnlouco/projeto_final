import os
from time import sleep

# 29. Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.

lista = []


def limparTela():
    os.system('cls')


def linha(tam = 40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())
    

def lerOpcao(lim_sup):
    while True:
        try:
            op = int(input('Digite um numero: '))
            if op >= 1 and op <= lim_sup:
                return op
            else:
                print('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m') 
        except(ValueError):
            print('\033[31mVoce nao digitou um numero, tente novamente com um NUMERO INTEIRO \033[m')
            continue


def menu(lista):
    limparTela()
    cabecalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}', flush=True)
        sleep(0.5)
        cont += 1
    print(linha())
    opc = lerOpcao(len(lista))
    return opc
    
    
# def escolha():
#     while True:
#         op = int(input('Digite um valor '))
#         if op == 1:
#             add = input('Escreva o que deseja adicionar: ')
#             lista.append(add)
#             return op
#         elif op == '2':
#             print(lista)
#             rem = input('Digite exatamente o que deseja remover: ')
#             lista.remove(rem)
            
#         elif op == '3':
#             print(lista)
            
#         elif op == '0':
#             print('Voce saiu !! ')
#             break
        
# menu()
