from Util import *


Visitantes = {}

def Participantes():
    while True:
        nome = input('Digite o NOME COMPLETO do participante: ')
        cpf = input('Digite o CPF do participante: ')
        email = input('Digite o E-MAIL do participante: ')
        
        Visitantes[cpf] = {'nome': nome, 'email': email}
        print(f'Os dados foram aceitos ')        
        if nome == '0':
            break
    lista_participantes = [x for x in Visitantes.items()]
    print(lista_participantes)

Participantes()        