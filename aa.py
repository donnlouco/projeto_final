from random import randint
'''
map. filter, reduste, 
cada evento possui nome unico

dicionario - eventos
dicionario dentro de lista e essa lista ter varios dicionarios(eventos)
dentro desse evento(dict) tera uma lista de participantes
[{evento1}, {evento1}, {evento1}, {evento1}, {evento1}]

listagem, imprimir dicionario e listas
eventos -- separados de participantes
participantes -- separados de eventos

listagem de participantes POR EVENTO

ver a remocao(pois pode ter participantes dentro dos eventos, TOMAR CUIDADO)

possibilidade de alterar dados do evento, participantes

SET para remover dados duplicados

pesquisar como pesquisar sobre DATA em python

'''

#AULA 11


'''
lambda function

chamadas de funcoes anonimas, funcoes indefinidas

sintaxe: lambda argumentos:(nao precisa usar parenteses, e nao precisa nomear a funcao): expressao(corpo da funcao) 
'''

dobro = lambda x: x * 2

print('exemplo - 1 dobro de 5:', dobro(5))


soma = lambda x, y: x + y
print('exemplo - 2 soma de 3 e 4:', soma(3, 4))


hipotenusa = lambda y, z: (y**2 + z**2)**(1/2)
print('exemplo - 3 hipotenusa de 3 e 4:', hipotenusa(3, 4))

# filter -------------- IMPORTANTISSIMA
# map  usa LAMBDA com filter e map

numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = filter(func, array)
pares = list(filter(lambda x: x % 2 == 0, numeros)) # o filter converte em um objeto, por isso convertemos em uma lista, para conseguir printar
print('exemplo - 4 apenas os pares dos numeros:', pares) #filter object at 0x0000021630B69D50> --- referencia do endereco q ele se encontra na memoria do PC




'''
gere 100 num rand (20 a 100), filtrar > 60
gere 100 num rand (20 a 100), filtrar > media
gere 100 num rand (20 a 100), filtrar < 25
'''

num = [randint(20, 100) for x in range(100)]

maiores60 = list(filter(lambda x: x > 60,num))
print('exemplo - 5 maiores q 60:', maiores60)

media = list(filter(lambda x: x > (sum(num) / len(num)), num))
print('exemplo - 6 media q 60:', media)

menores25= list(filter(lambda x: x < 25,num))
print('exemplo - 7 maiores q 25:', menores25)


# quadrado = list(map(func, array)) map PARA TRANSFORMACOES
quadrado = list(map(lambda x: x** 2 , numeros))


# sorted(pessoas, key = lambda x: x[1])
# para organizar em ordem crescent
pessoas = [('ana', 19), ('joao', 30), ('maria', 20)]

crescente = sorted (pessoas, key = lambda x: x[1])
decrescente = list(reversed(sorted(pessoas, key = lambda x: x[1])))

print(decrescente)
