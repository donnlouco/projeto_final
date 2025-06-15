from Util import *
from time import sleep
from Participantes import *


eventos = []


def cadastrar_eventos():
    evento = {}
    LimparTela()
    nome_evento = input('Digite o nome do Evento: ')
    data_evento = input('Digite a data do Evento: ')
    tema_evento = input('Digite o tema do Evento: ')
    local_evento = input('Digite o local do Evento: ')
    evento = {
        'Nome do Evento': nome_evento,
        'Data do Evento': data_evento,
        'Tema do Evento': tema_evento,
        'Local do Evento': local_evento,
        'Participantes': []
        }
    eventos.append(evento)
    LimparTela()
    print('Evento Cadastrado!!', flush=True)
    sleep(4)
    
    
def remover_evento():
    LimparTela()
    verificar_eventos()
    try:
        indice = int(input('Digite o NUMERO do EVENTO que deseja REMOVER: '))
        del eventos[indice]
    except(IndexError, ValueError):
        print ('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m')
    finally:
        print('Evento REMOVIDO com sucesso !!!')
        sleep(4)

    
def listar_eventos():
    for i, evento in enumerate(eventos):
        print(f"{i} - {evento['Nome do Evento']} | Data: {evento['Data do Evento']} | Tema: {evento['Tema do Evento']} | Local: {evento['Local do Evento']} | Participantes: {len(evento['participantes'])}")
        sair = input(f'Digite algo para voltar: ')


      
def verificar_eventos():
    if not eventos:
        print('Nao tem Eventos cadastrados, Cadastre 1 evento: ', flush=True)
        sleep(5)
        cadastrar_eventos()
        listar_eventos()
    else:
        listar_eventos()
        

def escolha_evento():
    LimparTela()
    listar_eventos()
    try:
        opcao = int(input('Selecione o EVENTO que deseja cadastrar o participante: '))
        evento = eventos[opcao]
    except(IndexError, ValueError):
        print ('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m')
    
