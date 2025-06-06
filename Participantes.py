from Util import *
from Eventos import *


Visitantes = {}

def cadastrar_participantes():
    LimparTela()
    while True:
        verificar_eventos()
        nome = input('Digite o NOME COMPLETO do participante: ')
        cpf = input('Digite o CPF do participante: ')
        email = input('Digite o E-MAIL do participante: ')
        preferencias = input('Digite os temas preferidos: ')
        Visitantes[cpf] = {'Nome': nome, 'Email': email, 'Preferencias Tematicas': preferencias}
        print(f'Os dados foram aceitos ')
        saida = input('Digite 0 se deseja parar de cadastrar: ')       
        if saida == '0':
            break
        
def listar_participantes():
    LimparTela()
    for lista in Visitantes.items():
        print(lista)


def remover_participantes ():
    LimparTela()
    remove = input()


