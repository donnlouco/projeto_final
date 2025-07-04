from Eventos import *
from time import sleep
from Util import *
from testes import eve
from testes import listar_eve
from random import randint
from faker import Faker

def cpf():
    while True:#um loop para o usuario ficar ate a ser concedido o acesso
        cpf = input('Digite o CPF do participante (APENAS NUMEROS): ')
        # isdigit() verifica se os dados da string sao apenas numeros(0-9), sem espacos ou -
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print('CPF INVALIDO, tente novamente')


def cadastrar_participantes():
    LimparTela()
    verificar_eventos()#verifica se tem eventos cadastrados e caso tennha os eventos, ele printa os eventos para facil compreensao do usuario
    opcao = lerOpcao(len(eventos)-1)#o usuario ira escolher o indice que ele deseja
    evento = eventos[opcao]#essa variavel agora e o indice do Evento
    
    LimparTela()
    Cabecalho(f'Cadastrar participantes no Evento: {evento['Nome']}') #mostra 
    while True:
        cpf_valor = cpf()
        if verificar_cpf(cpf_valor, evento):
            continue
        else:
            nome = input('Digite o NOME COMPLETO do participante: ')
            email = input('Digite o E-MAIL do participante: ')
            preferencias = input('Digite os temas preferidos: ')
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
    Cabecalho(f'Participantes do Evento: {evento['Nome']}')
    
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
    Cabecalho(f'Remover Participante do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]:
        LimparTela()
        print("Nenhum participante cadastrado.")
        
    usuario = cpf()
    if usuario in evento["Participantes"]:
        print(f'Participante {evento['Participantes'][usuario]["Nome"]} deletado com SUCESSO!!')
        del evento['Participantes'][usuario]
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
    Cabecalho(f'Participantes do Evento: {evento['Nome']}')
    
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
    else:
        print('CPF nao encontrado... ')

    sair = input(f'Pressione Enter para voltar...')


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


def alteracao_dados_participantes():
    LimparTela()
    Cabecalho('Alteracao de Dados')
    verificar_eventos()
    opcao = lerOpcao(len(eventos)-1)
    evento = eventos[opcao]
    
    LimparTela()    
    Cabecalho(f'Participantes do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]:
        LimparTela()
        print("Nenhum participante cadastrado.")

    
    usuario = cpf()#chave de acesso dos participantes
    LimparTela()
    if usuario in evento["Participantes"]: #se a chave esta nos participantes do evento selecionado
        pessoa = evento["Participantes"][usuario] #entao nos atribuimos essa chave a variavel = pessoa
        
        for chaves, dados in pessoa.items():
            print(f'{chaves}: {dados}')
            
        alterar = input(f'Qual dado deseja alterar? (Nome / Email / Preferencias Tematicas): ').upper()
        
        LimparTela()
        if alterar == 'NOME':
            pessoa['Nome'] = input('Digite o novo Nome: ')
            print('Dados alterados com sucesso!! ')
        elif alterar == 'EMAIL':
            pessoa['Email'] = input('Digite o novo Email: ')
            print('Dados alterados com sucesso!! ')
        elif alterar == 'PREFERENCIAS TEMATICAS':
            pessoa['Preferencias Tematicas'] = input('Digite uma nova preferencia: ')
            print('Dados alterados com sucesso!! ')
        else:
            print('Opcao invalida. ')
    else:
        LimparTela()
        print('CPF nao encontrado... ')
        
    sair = input(f'Pressione Enter para voltar...')