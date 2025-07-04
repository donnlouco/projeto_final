from Util import *
from time import sleep
from Participantes import *
from datetime import date
from datetime import datetime


eventos = [
    {
        "Nome": "Python Day",
        "Data": date(2025, 10, 25),
        "Tema": "Segurança Cibernética",
        "Local": "São Paulo",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}, 
                          '07610192199': {'Nome': 'Eduardo de Souza lima', 'Email': 'Edusk8.cba@gmail.com', 'Preferencias Tematicas': 'seinao'},
                          '07610192195': {'Nome': 'Eudes', 'Email': 'Edusk8.cba@gmail.com', 'Preferencias Tematicas': 'seinao'}}, 
        }, 
    {
        "Nome": "Tech Summit",
        "Data": date(2025, 6, 15),
        "Tema": "Transformação Digital",
        "Local": "Tres Lagoas",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}, 
                          '07610192199': {'Nome': 'Eduardo de Souza lima', 'Email': 'Edusk8.cba@gmail.com', 'Preferencias Tematicas': 'seinao'}},
         },
    {
        "Nome": "Autumn Day",
        "Data": date(2025, 7, 17),
        "Tema": "Inteligência Artificial (IA) e Aprendizado de Máquina",
        "Local": "Campo Grande",
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}},
    {
        "Nome": "Summer day",
        "Data": date(2025, 5, 11),
        "Tema": "Transformação Digital",
        "Local": "Rio de Janeiro",
        "Participantes": {}} 
]



def cadastrar_eventos():
    LimparTela()
    nome_evento = input('Digite o nome do Evento: ')
    data_evento = validar_data() #aqui temos um funcao de data, na qual verificamos se o usuario esta tentando colocar uma data antiga
    tema_evento = input('Digite o tema do Evento: ')
    local_evento = input('Digite o local do Evento: ')
    #armazenamos todos os dados que o usuario digitou em um dicionario (evento) e depois colocamos esse dicinario na lista EVENTOS
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
    verificar_eventos()# verifica se tem eventos cadastrados e caso tennha os eventos, ele printa os eventos para facil compreensao do usuario
    opcao = lerOpcao(len(eventos)-1) # o usuario ira escolher o indice que ele deseja
    evento = eventos[opcao] # armazena temporariamente o evento escolhido
    print(f'Evento {evento['Nome']} REMOVIDO com sucesso !!!')
    del eventos[opcao] # remove o evento da lista original
    sair = input(f'Pressione Enter para voltar...')

    
def listar_eventos():
    for i, evento in enumerate(eventos):
        print(f"{i} - {evento['Nome']} | Data: {evento['Data']} | Tema: {evento['Tema']} | Local: {evento['Local']} | Participantes: {len(evento['Participantes'])}")

        
        
def printar_eventos():
    for i, evento in enumerate(eventos): # printa todos evento informando seus indices
                print(f"{i} - {evento['Nome']} | Data: {evento['Data']} | Tema: {evento['Tema']} | Local: {evento['Local']} | Participantes: {len(evento['Participantes'])}")
    sair = input(f'Digite algo para voltar: ')

      
def verificar_eventos():
    if not eventos:# se nao tem nenhum evento, ele chama a funcao para cadastar
        print('Nao tem Eventos cadastrados, Cadastre 1 evento: ', flush=True) #precisa do flush=True para ter o sleep
        sleep(5)
        cadastrar_eventos()
        listar_eventos()
    else: # se tem evento, ele mostra os eventos com indices
        listar_eventos()
        
        

def alteracao_dados_eventos():
    LimparTela()
    Cabecalho('Alteracao de Dados')
    verificar_eventos()# para mostrar os eventos com indice
    opcao = lerOpcao(len(eventos)-1)# o usuario ira escolher o indice que ele deseja
    evento = eventos[opcao] # essa variavel agora e o indice do Evento
    
    LimparTela()    
    Cabecalho(f'Alteracoes do Evento: {evento['Nome']}') # nome do evento e em seguida mostramos os as chaves e valores do evento(menos participantes)
    
    print(f'Nome : {evento['Nome']}')
    print(f'Data : {evento['Data']}')
    print(f'Tema : {evento['Tema']}')
    print(f'Local : {evento['Local']}')
    
    alterar = input(f'Qual dado deseja alterar? (Nome / Data / Tema / Local): ').upper()
    
    LimparTela()
    if alterar == 'NOME': # se for nome, ele ira alterar o nome do evento
        evento['Nome'] = input('Digite o novo Nome do evento: ')
        print('Dados Alterados com sucesso')
    elif alterar == 'DATA': # se for data, ele ira alterar a data do evento
        evento['Data'] = validar_data()
        print('Dados Alterados com sucesso')
    elif alterar == 'TEMA': # se for tema, ele ira alterar o tema do evento
        evento['Tema'] = input('Digite o novo Tema do evento: ')
        print('Dados Alterados com sucesso')
    elif alterar == 'LOCAL': # se for nome, ele ira alterar o local do evento
        evento['Local'] = input('Digite o novo Local do evento: ')
        print('Dados Alterados com sucesso')
    else:
        print('Opcao invalida. ')
        

    sair = input(f'Pressione Enter para voltar...')    
    





