from Util import *
from time import sleep
from Participantes import *


eventos = [
    {
        'Nome': 'Python Day',
        'Data': '01-12-2025',
        'Tema': 'Segurança Cibernética',
        'Local': 'São Paulo',
        'Participantes': {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}
    },
    {
        'Nome': 'Tech Summit',
        'Data': '23-10-2025',
        'Tema': 'Transformação Digital',
        'Local': 'Tres Lagoas',
        'Participantes':  {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}
    },
    {
        'Nome': 'Autumn Day',
        'Data': '15-07-2025',
        'Tema': 'Inteligência Artificial (IA) e Aprendizado de Máquina',
        'Local': 'Campo Grande',
        'Participantes': {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}
    },
    {
        'Nome': 'Summer day',
        'Data': '11-05-2025',
        'Tema': 'Big Data e Analytics',
        'Local': 'Rio de Janeiro',
        'Participantes': {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}
    } 
]


def cadastrar_eventos():
    evento = {}
    LimparTela()
    nome_evento = input('Digite o nome do Evento: ')
    data_evento = input('Digite a data do Evento: ')
    tema_evento = input('Digite o tema do Evento: ')
    local_evento = input('Digite o local do Evento: ')
    evento = {
        'Nome': nome_evento,
        'Data': data_evento,
        'Tema': tema_evento,
        'Local': local_evento,
        'Participantes': {}
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
        print(f"{i} - {evento['Nome']} | Data: {evento['Data']} | Tema: {evento['Tema']} | Local: {evento['Local']} | Participantes: {len(evento['Participantes'])}")
        
        
def printar_eventos():
    for i, evento in enumerate(eventos):
        print(f"{i} - {evento['Nome']} | Data: {evento['Data']} | Tema: {evento['Tema']} | Local: {evento['Local']} | Participantes: {len(evento['Participantes'])}")
        sair = input('Digite algo para SAIR: ')

      
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
    
