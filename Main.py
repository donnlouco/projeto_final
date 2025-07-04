
from Menu import *
from Eventos import *
from Participantes import *
from Estatisticas import *

while True:
    resposta = MenuPrincipal(['Participantes', 'Evento', 'Estatisticas', 'Sair'])
    if resposta == 0:
        MenuParticipantes(['Cadastro', 'Atualizacao do cadastro', 'Remocao de participantes', 'Busca de participantes por CPF', 'Voltar'])
    elif resposta == 1:
        MenuEvento(['Cadastro de Eventos', 'Alteracao de eventos', 'Remocao de eventos','Listagem de participantes por evento', 'Voltar'])
    elif resposta == 2:
        MenuEstatisticas(['Media de participantes por evento', 'Temas mais frequentes', 'Participantes mais ativos', 'Listar Eventos por Tema', 'Listar Eventos por Data', 'Eventos para possivel cancelamento', 'Voltar'])
    elif resposta == 3:
        print('Voce escolheu sair do programa !!!')
        break