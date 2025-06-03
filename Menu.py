from Util import *
from time import sleep

def MenuPrincipal(lista):
    LimparTela()
    Cabecalho('Menu de Navegacao')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}', flush=True)
        sleep(0.5)
        cont += 1
    opc = lerOpcao(len(lista))
    return opc
    
    
def MenuParticipantes(lista):
    LimparTela()
    Cabecalho('Menu dos Participantes')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}', flush=True)
        sleep(0.5)
        cont += 1
    opc = lerOpcao(len(lista))
    return opc
    

def MenuEvento(lista):
    LimparTela()
    Cabecalho('Menu de Eventos')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}', flush=True)
        sleep(0.5)
        cont += 1
    opc = lerOpcao(len(lista))
    return opc
    
    
def MenuEstatisticas(lista):
    LimparTela()
    Cabecalho('Estatisticas')
    cont = 1
    for item in lista:
        print(f'{cont} - {item}', flush=True)
        sleep(0.5)
        cont += 1
    opc = lerOpcao(len(lista))
    return opc