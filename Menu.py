from Util import *


def MenuPrincipal():
    LimparTela()
    Cabecalho('Menu de Navegacao')
    print('1 - Participantes')
    print('2 - Eventos')
    print('3 - Estatisticas')
    print('4 - Sair')
    opc = lerOpcao(4)
    return opc
    
    
def MenuParticipantes():
    LimparTela()
    Cabecalho('Menu dos Participantes')
    print('1 - Cadastro')
    print('2 - Atualizacao')
    print('3 - Remocao')
    print('4 - Busca')
    print('5 - Voltar')
    opc = lerOpcao(5)
    return opc
    

def MenuEvento():
    LimparTela()
    Cabecalho('Menu de Eventos')
    print('1 - Cadastro')
    print('2 - Alteracao')
    print('3 - Remocao')
    print('4 - Busca')
    print('5 - Voltar')
    opc = lerOpcao(5)
    return opc
    
    
def MenuEstatisticas():
    LimparTela()
    Cabecalho('Estatisticas')
    print('1 - Quantos Eventos Cada Tema Possui')
    print('2 - Media de Participantes Por Tema')
    print('3 - Temas Mais Frequentes')
    print('4 - Participantes Mais Ativos')
    print('5 - Voltar')
    opc = lerOpcao(5)
    return opc