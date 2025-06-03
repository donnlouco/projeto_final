from biblioteca import *
from Menu import *

while True:
    resposta = MenuPrincipal()
    if resposta == 1:
        MenuParticipantes()
    elif resposta == 2:
        MenuEvento()
    elif resposta == 3:
        MenuEstatisticas()
    elif resposta == 4:
        print('Voce escolheu sair do programa !!!')
        break