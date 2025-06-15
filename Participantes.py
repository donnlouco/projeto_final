from Eventos import *
from time import sleep
from Util import *
from testes import eve
from testes import listar_eve

participantes = []

def cpf():
    while True:
        cpf = input('Digite o CPF do participante (APENAS NUMEROS): ')
        if cpf.isdigit and len(cpf) == 11:
            print('CPF aceito!!')
            return cpf
        else:
            print('CPF INVALIDO, tente novamente')


def cadastrar_participantes():
    Visitantes = {}
    LimparTela()
    # verificar_eventos()
    listar_eve()
    try:
        opcao = int(input('Selecione o EVENTO que deseja cadastrar o participante: '))
        evento = eve[opcao]
    except(IndexError, ValueError):
        print ('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m')
        return
        
    while True:
        cpf_valor = cpf()
        nome = input('Digite o NOME COMPLETO do participante: ')
        email = input('Digite o E-MAIL do participante: ')
        preferencias = input('Digite os temas preferidos: ')
        numero = input('Digite um numero para contato:(COM DDD) ')
        Visitantes = {'CPF': cpf_valor, 'Nome': nome, 'Email': email,'Contato': numero, 'Preferencias Tematicas': preferencias}
        print(f'Os dados foram aceitos ')
        evento["participantes"].append(Visitantes)
        saida = input('Digite 0 se deseja parar de cadastrar: ')       
        if saida == '0':
            break
        
        
def listar_participantes():
    LimparTela()
    Cabecalho('Lista de participantes')
    listar_eve()
    try:
        opcao = int(input('Selecione o EVENTO que deseja listar os participantes: '))
        evento = eve[opcao]
    except(IndexError, ValueError):
        print ('\033[31mVoce nao digitou uma opcao valida, tente novamente \033[m')
        return opcao
        
    print(f'Participantes do Evento{evento['nome']}')
    
    if not evento["participantes"]:
        print("Nenhum participante cadastrado.")
        return

    for i, pessoas in enumerate(evento['participantes']):
        print(f"{i}. Nome: {pessoas['Nome']} | Email: {pessoas['Email']} | CPF: {pessoas['CPF']} | Preferencias tematicas: {pessoas['Preferencias Tematicas']}")
        sair = input(f'Digite algo para voltar: ')


def remover_participantes ():
    LimparTela()
    remove = input()
    
    
def verificar_cpf():
    pass   



