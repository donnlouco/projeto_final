from Util import *
from time import sleep

evento = {}


def cadastrar_eventos():
    LimparTela()
    nome_evento = input('Digite o nome do Evento: ')
    data_evento = input('Digite a data do Evento: ')
    horario_inicio = input('Digite o horario do inicio do Evento: ')
    horario_final = input('Digite o horario do final do Evento: ')
    evento[nome_evento] = {'Data do Evento': data_evento, 'Horario do Inicio': horario_final, 'Horario de Encerramento': horario_final}

def verificar_eventos():
    if not evento:
        print('Nao tem Eventos cadastrados', flush=True)
        sleep(3)
        cadastrar_eventos()   
    else:
        print(evento)
        


    
