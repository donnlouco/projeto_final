from Eventos import *
from time import sleep
from Util import *
from testes import eve
from testes import listar_eve
from random import randint
from faker import Faker

def cpf():
    while True:# um loop para o usuario ficar ate a ser concedido o acesso
        cpf = input('Digite o CPF do participante (APENAS NUMEROS): ')
        # isdigit() verifica se os dados da string sao apenas numeros(0-9), sem espacos ou -
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print('CPF INVALIDO, tente novamente')


def cadastrar_participantes():
    LimparTela()
    verificar_eventos()# verifica se tem eventos cadastrados e caso tennha os eventos, ele printa os eventos para facil compreensao do usuario
    opcao = lerOpcao(len(eventos)-1)# o usuario ira escolher o indice que ele deseja
    evento = eventos[opcao]# essa variavel agora tem o indice do evento
    
    LimparTela()
    Cabecalho(f'Cadastrar participantes no Evento: {evento['Nome']}')
    while True: # fazemos um loop para adicionar o participante
        cpf_valor = cpf() # chama a funcao cpf e armazena na variavel
        if verificar_cpf(cpf_valor, evento): # verifica se ja tem o cpf digitado, se tiver o cpf,
            # a funcao retorna true e o (continue) faz o código voltar para o início do while, ou seja, pede outro CPF.
            continue
        # se o CPF não estiver cadastrado, o resultado é false, então o else é executado
        else:
            nome = input('Digite o NOME COMPLETO do participante: ') # nome para o participante
            email = input('Digite o E-MAIL do participante: ') # email para o participante
            preferencias = input('Digite os temas preferidos: ')  # Pede as preferências temáticas
            print(f'Os dados foram aceitos ')
            evento["Participantes"][cpf_valor] = {'Nome': nome, 'Email': email, 'Preferencias Tematicas': preferencias} # Adiciona o participante ao dicionário do evento
            saida = input('Digite 0 se deseja parar de cadastrar: ') # Pergunta se deseja parar      
            if saida == '0': # Se digitar 0, encerra o loop
                break
        
        
def listar_participantes():
    LimparTela()
    Cabecalho('Lista de participantes')
    verificar_eventos()# verifica se tem eventos cadastrados e caso tennha os eventos, ele printa os eventos para facil compreensao do usuario
    opcao = lerOpcao(len(eventos)-1)# o usuario ira escolher o indice que ele deseja
    evento = eventos[opcao]# essa variavel agora tem o indice do evento
    
    LimparTela()   
    Cabecalho(f'Participantes do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]:# se nao tem participantes no evento, ele informa que nao tem participantes
        LimparTela()
        print("Nenhum participante cadastrado.")
        sair = input(f'Pressione Enter para voltar...')
        return

    for i, pessoas in evento['Participantes'].items():# fazemos um lopp para mostrar todos os participantes dentro do evento selecionado
        print(f"CPF: {i} . Nome: {pessoas['Nome']} | Email: {pessoas['Email']} | | Preferencias tematicas: {pessoas['Preferencias Tematicas']}")
    sair = input(f'Pressione Enter para voltar...')


def remover_participantes ():
    LimparTela()
    Cabecalho('Remocao de Participantes')
    verificar_eventos()# verifica se tem eventos cadastrados e caso tennha os eventos, ele printa os eventos para facil compreensao do usuario
    opcao = lerOpcao(len(eventos)-1)# o usuario ira escolher o indice que ele deseja
    evento = eventos[opcao]# essa variavel agora tem o indice do evento
    
    LimparTela()
    Cabecalho(f'Remover Participante do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]:# se nao tem participantes no evento, ele informa que nao tem participantes
        LimparTela()
        print("Nenhum participante cadastrado.")
        sair = input(f'Pressione Enter para voltar...')
        return
        
    usuario = cpf() # chama a funcao cpf e armazena na variavel usuario
    if usuario in evento["Participantes"]: #s e a chave(usuario(cpf)) esta nos participantes do evento
        print(f'Participante {evento['Participantes'][usuario]["Nome"]} deletado com SUCESSO!!') # informa que o usuario foi removido
        del evento['Participantes'][usuario] #remove o usuario
    else: # se nao tem o usuario(cpf) no evento escolhido
        print('Nao tem Participante com esse CPF')
    sair = input(f'Pressione Enter para voltar...')

    
    
def verificar_cpf(cpf, evento):
    if cpf in evento['Participantes']: # Verifica se o CPF já existe no dicionário de participantes do evento
        print('CPF ja cadastrado!!')
        return True # Retorna True, indicando que o CPF já está cadastrado
    return False # Se o CPF não estiver cadastrado, retorna False
    


def busca_por_cpf():
    LimparTela()
    Cabecalho('Busca pelo CPF')
    verificar_eventos() # mostra a lista de eventos disponíveis (para o usuário escolher)
    opcao = lerOpcao(len(eventos)-1) # ve a opção do usuário, que deve ser um índice válido na lista de eventos
    evento = eventos[opcao] # seleciona o evento escolhido pelo usuário
    
    LimparTela()    
    Cabecalho(f'Participantes do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]: #verifica se tem participante dentro do evento
        LimparTela()
        print("Nenhum participante cadastrado.")
        sair = input(f'Pressione Enter para voltar...')
        return
    
    usuario = cpf() # pede o CPF que o usuário deseja buscar
    if usuario in evento["Participantes"]: # verifica se o CPF está na lista de participantes
        pessoas = evento["Participantes"][usuario] # entao nos atribuimos essa chave a variavel = pessoa
        LimparTela()
        print(f'CPF: {usuario}')
        print(f'Nome: {pessoas['Nome']}')
        print(f'Email: {pessoas['Email']}')
        print(f'Preferencias tematicas: {pessoas['Preferencias Tematicas']}')
    else:
        print('CPF nao encontrado... ') # Mensagem caso o CPF não esteja cadastrado no evento

    sair = input(f'Pressione Enter para voltar...')


def alteracao_dados_participantes():
    LimparTela()
    Cabecalho('Alteracao de Dados')
    verificar_eventos() # mostra a lista de eventos disponíveis (para o usuário escolher)
    opcao = lerOpcao(len(eventos)-1) # ve a opção do usuário, que deve ser um índice válido na lista de eventos
    evento = eventos[opcao] # seleciona o evento escolhido pelo usuário
    
    LimparTela()    
    Cabecalho(f'Participantes do Evento: {evento['Nome']}')
    
    if not evento["Participantes"]:
        LimparTela()
        print("Nenhum participante cadastrado.")
        sair = input(f'Pressione Enter para voltar...')
        return

    usuario = cpf()# chave de acesso dos participantes
    LimparTela()
    if usuario in evento["Participantes"]: # verifica se o CPF está na lista de participantes
        pessoa = evento["Participantes"][usuario] # entao nos atribuimos essa chave a variavel = pessoa
        
        for chaves, dados in pessoa.items(): # mostra os dados atuais do participante
            print(f'{chaves}: {dados}')
            
        # pergunta ao usuário qual campo deseja alterar   
        alterar = input(f'Qual dado deseja alterar? (Nome / Email / Preferencias Tematicas): ').upper()
        
        LimparTela()
        if alterar == 'NOME': # se o usuário quiser alterar o nome
            pessoa['Nome'] = input('Digite o novo Nome: ')
            print('Dados alterados com sucesso!! ')
        elif alterar == 'EMAIL': # se o usuário quiser alterar o e-mail
            pessoa['Email'] = input('Digite o novo Email: ')
            print('Dados alterados com sucesso!! ')
        elif alterar == 'PREFERENCIAS TEMATICAS': # se quiser alterar as preferência
            pessoa['Preferencias Tematicas'] = input('Digite uma nova preferencia: ')
            print('Dados alterados com sucesso!! ')
        else: 
            print('Opcao invalida. ') # caso o usuário digite algo que não seja esperado
    else:
        LimparTela()
        print('CPF nao encontrado... ') # mensagem caso o CPF não esteja cadastrado no evento
        
    sair = input(f'Pressione Enter para voltar...')