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
    valor = int(input('Qual o minimo de vezes para filtragem: '))
    mais_ativos = Counter(nomes).most_common()
    
    filtragem = list(filter(lambda x: x[1] >= valor, mais_ativos))# fazemos uma filtragem com x[1](quantidade do counter) >= ao valor que sera informado pelo usuario
    
    if filtragem: # se tem filtragem, fazemos um (for) rodando eles e printando a quantidade e o nome
        for nome, qntd in filtragem:
            print(f'-- {nome}, Quantidade: {qntd}')
    else: # se nao tem pessoas na filtragem, retornamos o print
        print(f'Nao tem participantes com o valor minimo de {valor}')
    sair = input(f'Pressione Enter para voltar...')


def temas_mais_frequentes():
    LimparTela()
    temas = []
    for evento in eventos:
        temas.append(evento['Tema'])# para cada tema de 1 evento, nos adicionamos essa string(tema) no temas ali em cima, entao estamos listando todos os temas dos eventos
            
    temas_ativos = Counter(temas).most_common() # aqui estamos contando os temas
    
    for nome, qntd in temas_ativos:# apenas printando os temas, com nome do tema e quantidade
        print(f'{nome}, {qntd}')
    sair = input(f'Pressione Enter para voltar...')
        


def possivel_cancelamento():
    LimparTela()
    Cabecalho('Eventos com menos de 2 participantes')
    
    lista = [x for x in eventos if len(x['Participantes']) < 2]# faz um compreensao de lista que nos informa se um evento(x) tem menos de 2 participantes (len(x['Participantes']))
    
    if lista:# se tem valor(evento) na lista, nos printamos cada evento, informando as informacoes
        for nome in lista:
            print(f"Nome: {nome['Nome']} | Data: {nome['Data']} | Tema: {nome['Tema']} | Local: {nome['Local']}")
            print(Linha())
    else:# se nao tem nenhum valor(evento) na lista, ele informa
        print('Nao tem evento com menos de 2 pessoas')
    sair = input(f'Pressione Enter para voltar...')
    
    
def media_participantes_evento():
    LimparTela()
    Cabecalho('Media de participantes por evento')
    
    pessoas = [len(x['Participantes']) for x in eventos]# aqui nos listamos a quantidade de pessoas em cada evento em uma lista
    
    media = sum(pessoas) / len(eventos) # fazemos a soma de pessoas da lista e dividimos pela quantidade de eventos
    
    print(f'Media de participantes por evento: {media} pessoas')
    sair = input(f'Pressione Enter para voltar...')
    

def filtragem_tema():
    LimparTela()
    Cabecalho('Filtragem pelo Tema')
    todos_temas = [x['Tema'] for x in eventos] # printa todos os temas dos eventos
    print(todos_temas)
    tema = input('Informe o tema que deseja procurar: ').lower()
    
    evento_filtrado = [x for x in eventos if tema in x['Tema'].lower()]# cada x e um evento, entao se o tema aparecer em um evento (x['tema]), ele fica armazenado aq
    
    LimparTela()
    if evento_filtrado: # se tem evento com o tema, roda o arquivo
        for evento in evento_filtrado:
            print(f'Nome: {evento['Nome']}')
            print(f'Data: {evento['Data']}')
            print(f'Tema: {evento['Tema']}')
            print(f'Local: {evento['Local']}')
            print('')
    else:
        print('Tema nao encontrado nos Eventos disponiveis!! ')
        
    sair = input(f'Pressione Enter para voltar...') 
    
    
def filtragem_data():
    LimparTela()
    Cabecalho('Filtragem por Datas')
    print('Escolha a Data inicial')
    inicio = data()
    print('Escolha a Data final')
    final = data()
    
    data_min = min(inicio, final)# aqui pega a menor data, dentro dos parametros (inicio, final) garante que mesmo q o usuario inverta as datas
    data_max = max(inicio, final)# aqui pega a maior data, dentro dos parametros (inicio, final) garante que mesmo q o usuario inverta as datas
    
    evento_filtrado = [x for x in eventos if data_min <= x['Data'] <= data_max]
    
    evento_filtrado = sorted(evento_filtrado, key=lambda x: x['Data'])# x representa cada evento da lista, x['Data'] é a chave de ordenação (a data associada ao evento).
          
    LimparTela()
    if evento_filtrado: # se tem evento dentro das datas informadas
        for evento in evento_filtrado: # printa os eventos
            print(f'Nome: {evento['Nome']}, Data: {evento['Data']}, Tema: {evento['Tema']}, Local: {evento['Local']}')    

    else: # se nao tem eventos nessa faixa de datas
        print(f'Nao temos Eventos nessa faixa de Datas!! ')
        
    sair = input(f'Pressione Enter para voltar...')  
