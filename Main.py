from biblioteca import *
from Menu import *
from Eventos import *
from Participantes import *

while True:
    resposta = MenuPrincipal(['Participantes', 'Evento', 'Estatisticas', 'Sair'])
    if resposta == 0:
        MenuParticipantes(['Cadastro', 'Atualizacao', 'Remocao', 'Listagem', 'Voltar'])
    elif resposta == 1:
        MenuEvento(['Cadastro', 'Alteracao', 'Remocao', 'Busca', 'Voltar'])
    elif resposta == 2:
        MenuEstatisticas(['Media de participantes por evento', 'Temas mais frequentes', 'Participantes mais ativos', 'Quantos eventos cada tema possui', 'Voltar'])
    elif resposta == 3:
        print('Voce escolheu sair do programa !!!')
        break