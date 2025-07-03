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
        "Participantes": {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}} 
]



def cadastrar_eventos():
    LimparTela()
    nome_evento = input('Digite o nome do Evento: ')
    data_evento = validar_data()
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
    

def filtragem_tema():
    LimparTela()
    Cabecalho('Filtragem pelo Tema')
    todos_temas = [x['Tema'] for x in eventos]
    print(todos_temas)
    tema = input('Informe o tema que deseja procurar: ')
    
    evento_filtrado = [x for x in eventos if tema in x['Tema']]#cada x e um evento, entao se o tema aparecer em um evento (x['tema]), ele fica armazenado aq
    
    if evento_filtrado: # se tem evento com o tema, roda o arquivo
        for evento in evento_filtrado:
            LimparTela()
            print(f'Nome: {evento['Nome']}')
            print(f'Nome: {evento['Data']}')
            print(f'Nome: {evento['Tema']}')
            print(f'Nome: {evento['Local']}')
            print('')
    else:
        print('Tema nao encontrado nos Eventos disponiveis!! ')
        
    sair = input(f'Pressione Enter para voltar...')  



def filtragem_data():
    LimparTela()
    Cabecalho('Filtragem por Datas')
    print('Escolha a Data inicial')
    inicio = data()
    print('Escolha a Data final')
    final = data()
    
    data_min = min(inicio, final)#aqui pega a menor data, dentro dos parametros (inicio, final) garante que mesmo q o usuario inverta as datas
    data_max = max(inicio, final)#aqui pega a maior data, dentro dos parametros (inicio, final) garante que mesmo q o usuario inverta as datas
    
    evento_filtrado = [x for x in eventos if data_min <= x['Data'] <= data_max]
    
    evento_filtrado = sorted(evento_filtrado, key=lambda x: x['Data'])# x representa cada evento da lista, x['Data'] é a chave de ordenação (a data associada ao evento).
          
    LimparTela()
    if evento_filtrado:
        for evento in evento_filtrado:
            print(f'Nome: {evento['Nome']}, Data: {evento['Data']}, Tema: {evento['Tema']}, Local: {evento['Local']}')    

    else:
        print(f'Nao temos Eventos nessa faixa de Datas!! ')
        
    sair = input(f'Pressione Enter para voltar...') 



def possivel_cancelamento():
    LimparTela()
    Cabecalho('Eventos com menos de 2 participantes')
