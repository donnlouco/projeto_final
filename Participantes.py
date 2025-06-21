from Eventos import *
from time import sleep
from Util import *
from testes import eve
from testes import listar_eve
from random import randint
from faker import Faker

def cpf():
    while True:
        cpf = input('Digite o CPF do participante (APENAS NUMEROS): ')
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print('CPF INVALIDO, tente novamente')


def cadastrar_participantes():
    LimparTela()
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    
    # for nome in range(5):    
    while True:
        cpf_valor = cpf()
        if verificar_cpf(cpf_valor, evento):
            continue
        else:
            nome = input('Digite o NOME COMPLETO do participante: ')
            email = input('Digite o E-MAIL do participante: ')
            preferencias = input('Digite os temas preferidos: ')
            # nome = nome_aleatorio()
            # email = email_aleatorio()
            preferencias = ('Tech tech')
            print(f'Os dados foram aceitos ')
            evento["Participantes"][cpf_valor] = {'Nome': nome, 'Email': email, 'Preferencias Tematicas': preferencias}
            saida = input('Digite 0 se deseja parar de cadastrar: ')       
            if saida == '0':
                break
        
        
def listar_participantes():
    LimparTela()
    Cabecalho('Lista de participantes')
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    LimparTela()   
    print(f'Participantes do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]:
        LimparTela()
        print("Nenhum participante cadastrado.")

    for i, pessoas in evento['Participantes'].items():
        print(f"CPF: {i} . Nome: {pessoas['Nome']} | Email: {pessoas['Email']} | | Preferencias tematicas: {pessoas['Preferencias Tematicas']}")
    sair = input(f'Pressione Enter para voltar...')


def remover_participantes ():
    LimparTela()
    Cabecalho('Remocao de Participantes')
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    
    LimparTela()
    print(f'Remover Participante do Evento: {evento['Nome']}')
    if not evento["Participantes"]:
        LimparTela()
        print("Nenhum participante cadastrado.")
        
    usuario = cpf()
    if usuario in evento["Participantes"]:
        del evento['Participantes'][usuario]
        print('Participante deletado com SUCESSO!!')
    else:
        print('Nao tem Participante com esse CPF')
    sair = input(f'Pressione Enter para voltar...')

    
    
def verificar_cpf(cpf, evento):
    if cpf in evento['Participantes']:
        print('CPF ja cadastrado!!')
        return True
    return False
    


def busca_por_cpf():
    LimparTela()
    Cabecalho('Busca pelo CPF')
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    
    LimparTela()    
    print(f'Participantes do Evento: {evento['Nome']}')
    if not evento["Participantes"]:
        LimparTela()
        print("Nenhum participante cadastrado.")
    
    usuario = cpf()
    if usuario in evento["Participantes"]:
        pessoas = evento["Participantes"][usuario]
        LimparTela()
        print(f'CPF: {usuario}')
        print(f'Nome: {pessoas['Nome']}')
        print(f'Email: {pessoas['Email']}')
        print(f'Preferencias tematicas: {pessoas['Preferencias Tematicas']}')

    sair = input(f'Digite algo para voltar: ')


def cpf_aleatorio():
    a = [str(randint(0, 9)) for _ in range(11)]
    cpf = ''.join(a)
    return cpf


def nome_aleatorio():
    fake = Faker()
    nome_al = fake.name()
    return nome_al


def email_aleatorio():
    fake = Faker()
    nome_al = 'x'
    email_al = '@gmail.com'.join(nome_al)
    return email_al
