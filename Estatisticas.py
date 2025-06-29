from Eventos import *
from Participantes import *
from collections import Counter


def participantes_mais_ativos():
    LimparTela()
    nomes = []
    for evento in eventos:
        # nos vamos correr os eventos com EVENTO
        # dentro de CADA EVENTO, nos selecionamos a key(participantes) e queremos apenas os valores(nomes, email, preferencias tematicas)
        for participantes in evento['Participantes'].values():
            # nos adicionamos cada participante com a chave['Nome] = NOME a uma lista de nomes
            nomes.append(participantes['Nome'])
    
    # counter serve para armazenar e contar os elementos, as chaves sao os nomes e os valores sao a quantidade
    # most common é um método para extrair e apresentar os resultados de forma ordenada   
    mais_ativos = Counter(nomes).most_common()
    
    valor = int(input('Qual o minimo de vezes para filtragem: '))
    for nome, qntd in mais_ativos:
        if qntd >= valor:
            print(f'-- {nome}, Quantidade: {qntd}')
    sair = input(f'Pressione Enter para voltar...')


def temas_mais_frequentes():
    LimparTela()
    temas = []
    for evento in eventos:
        temas.append(evento['Tema'])
            
    temas_ativos = Counter(temas).most_common()
    
    for nome, qntd in temas_ativos:
        print(f'{nome}, {qntd}')
    sair = input(f'Pressione Enter para voltar...')
        


        
