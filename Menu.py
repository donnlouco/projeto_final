from Util import *
from time import sleep
from Participantes import *
from Eventos import *
from Estatisticas import*


def MenuPrincipal(lista):
    LimparTela()
    Cabecalho('Menu de Navegacao')
    
    for i, item in enumerate(lista):
        print(f'{i} - {item}', flush=True)
        sleep(0.1)
        
    opc = lerOpcao(len(lista) - 1)
    return opc
    
    
def MenuParticipantes(lista):
    LimparTela()
    Cabecalho('Menu dos Participantes')
    
    for i, item in enumerate(lista):
        print(f'{i} - {item}', flush=True)
        sleep(0.1)
        
    opc = lerOpcao(len(lista) - 1)
    if opc == 0:
        cadastrar_participantes()
        
    elif opc == 1:
        alteracao_dados_participantes()
        
    elif opc == 2:
        remover_participantes()
        
    elif opc == 3:
        busca_por_cpf()
        
    return opc
    

def MenuEvento(lista):
    LimparTela()
    Cabecalho('Menu de Eventos')
    
    for i, item in enumerate(lista):
        print(f'{i} - {item}', flush=True)
        sleep(0.1)
        
    opc = lerOpcao(len(lista) - 1)
    if opc == 0:
        cadastrar_eventos()
    elif opc == 1:
        alteracao_dados_eventos()
        
    elif opc == 2:
        remover_evento()
        
    elif opc == 3:
        filtragem_tema()
        
    elif opc == 4:
        listar_participantes()
        
    return opc
    
    
def MenuEstatisticas(lista):
    LimparTela()
    Cabecalho('Estatisticas')
    
    for i, item in enumerate(lista):
        print(f'{i} - {item}', flush=True)
        sleep(0.1)
        
    opc = lerOpcao(len(lista) - 1)
    if opc == 0:
        pass
    elif opc == 1:
        temas_mais_frequentes()
        
    elif opc == 2:
        participantes_mais_ativos()
        
    elif opc == 3:
        listar_participantes()
        
    return opc
