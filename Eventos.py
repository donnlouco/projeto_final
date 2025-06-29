from Util import *
from time import sleep
from Participantes import *


eventos = [
    {
        "Nome": "Python Day",
        "Data": "01-12-2025",
        "Tema": "Segurança Cibernética",
        "Local": "São Paulo",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}, 
                          '07610192199': {'Nome': 'Eduardo de Souza lima', 'Email': 'Edusk8.cba@gmail.com', 'Preferencias Tematicas': 'seinao'}}, 
        }, 
    {
        "Nome": "Tech Summit",
        "Data": "23-10-2025",
        "Tema": "Transformação Digital",
        "Local": "Tres Lagoas",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}, 
                          '07610192199': {'Nome': 'Eduardo de Souza lima', 'Email': 'Edusk8.cba@gmail.com', 'Preferencias Tematicas': 'seinao'}},
         },
    {
        "Nome": "Autumn Day",
        "Data": "15-07-2025",
        "Tema": "Inteligência Artificial (IA) e Aprendizado de Máquina",
        "Local": "Campo Grande",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}},
    {
        "Nome": "Summer day",
        "Data": "11-05-2025",
        "Tema": "Big Data e Analytics",
        "Local": "Rio de Janeiro",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}} 
]



def cadastrar_eventos():
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
    Cabecalho('Remover Evento')
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    print(f'Evento {evento['Nome']} REMOVIDO com sucesso !!!')
    del evento
    sair = input(f'Pressione Enter para voltar...')

    
def listar_eventos():
    for i, evento in enumerate(eventos):
        print(f"{i} - {evento['Nome']} | Data: {evento['Data']} | Tema: {evento['Tema']} | Local: {evento['Local']} | Participantes: {len(evento['Participantes'])}")

        
        
def printar_eventos():
    for i, evento in enumerate(eventos):
                print(f"{i} - {evento['Nome']} | Data: {evento['Data']} | Tema: {evento['Tema']} | Local: {evento['Local']} | Participantes: {len(evento['Participantes'])}")
    sair = input(f'Digite algo para voltar: ')

      
def verificar_eventos():
    if not eventos:
        print('Nao tem Eventos cadastrados, Cadastre 1 evento: ', flush=True)
        sleep(5)
        cadastrar_eventos()
        listar_eventos()
    else:
        listar_eventos()
        
        

def alteracao_dados_eventos():
    LimparTela()
    Cabecalho('Alteracao de Dados')
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    
    LimparTela()    
    Cabecalho(f'Alteracoes do Evento: {evento['Nome']}')
    
    print(f'Nome : {evento['Nome']}')
    print(f'Data : {evento['Data']}')
    print(f'Tema : {evento['Tema']}')
    print(f'Local : {evento['Local']}')
    
    alterar = input(f'Qual dado deseja alterar? (Nome / Data / Tema / Local): ').upper()
    
    LimparTela()
    if alterar == 'NOME':
        evento['Nome'] = input('Digite o novo Nome do evento: ')
        print('Dados Alterados com sucesso')
    elif alterar == 'DATA':
        evento['Data'] = input('Digite a nova Data do evento: ')
        print('Dados Alterados com sucesso')
    elif alterar == 'TEMA':
        evento['Tema'] = input('Digite o novo Tema do evento: ')
        print('Dados Alterados com sucesso')
    elif alterar == 'LOCAL':
        evento['Local'] = input('Digite o novo Local do evento: ')
        print('Dados Alterados com sucesso')
    else:
        print('Opcao invalida. ')
        

    sair = input(f'Pressione Enter para voltar...')    
    
