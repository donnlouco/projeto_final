import os
from datetime import datetime
from datetime import date


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
            

def data():
    while True:
        data_entrada = input('Informe a data do Evento: (DD/MM/AAAA) ')
        data_limpa = data_entrada.strip()# Ele remove todos os espaços em branco
        try:
            # o "%d/%m/%Y" o Y tem que ser MAIUSCULO, se nao da erro, meu DEUSSSSSSSSS
            data_valida = datetime.strptime(data_limpa, '%d/%m/%Y').date()
            return data_valida
        except(ValueError):
            print('Tente novamente com o formato (DD/MM/AAAA)')
            
            
def validar_data():
    data_atual = date.today()#pega a data atual e amarmazena em um variavel
    while True:
        data_entrada = input('Informe a data do Evento: (DD/MM/AAAA) ')
        data_limpa = data_entrada.strip()
        try:
            data_valida = datetime.strptime(data_limpa, '%d/%m/%Y').date()
            if data_valida >= data_atual: # se a data digitada pelo usuario for maior que a atual, ela aceita, caso contrario, pedira para o usuario digitar novamente
                return data_valida #ate o usuario colocar uma data correta
            else:
                print('Data antiga, infome uma nova data')
        except(ValueError):
            print('Tente novamente com o formato (DD/MM/AAAA)')