import os
from datetime import datetime
from datetime import date


def LimparTela():
    os.system('cls') #para limpar a tela


def Linha(tam = 80): #faz uma linha
    return '-' * tam


def Cabecalho(txt):
    print(Linha())
    print(txt.center(80))#centraliza e recebe um texto
    print(Linha())
    

def lerOpcao(lim_sup):
    while True: #fazemos um loop que nao deixa o usuario sair ate ele digitar o que esperamos
        try: # Se o usuário digitar algo como "abc" ou "5.2", isso vai gerar um erro — e o except será acionado.
            valor = int(input('Digite um numero: ')) #recebemos o valor do usuario
            # se o valor for maior ou igual a 0(entao ele nao aceita numeros negativos) e se o valor for menor ou igual com o limite do parametro que escolhemos
            if valor >= 0 and valor <= lim_sup: 
                return valor# se as condicoes forem aceitas ele retorna valor
            else:
                print('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m') 
        except(ValueError, IndexError): # Se o usuario digitar uma letra, ou caracteres ira dar (valueerror), com expect o programa nao quebra
            #indexerror sera para acessarmos as listas, como a de eventos
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