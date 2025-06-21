eve = [
    {
        "nome": "Python Day",
        "data": "01-12-2025",
        "tema": "Segurança Cibernética",
        "local": "São Paulo",
        "participantes": {'07610192198':
                {'Nome': 'Vinicius henrique de souza lima',
                 'Email': 'Vinisk8.cba@gmail.com',
                 'Preferencias Tematicas': 'Tech'}}
    },
    {
        "nome": "Tech Summit",
        "data": "23-10-2025",
        "tema": "Transformação Digital",
        "local": "Tres Lagoas",
        "participantes":  {'07610192198':
                {'Nome': 'Vinicius henrique de souza lima',
                 'Email': 'Vinisk8.cba@gmail.com',
                 'Preferencias Tematicas': 'Tech'}}
    },
    {
        "nome": "Autumn Day",
        "data": "15-07-2025",
        "tema": "Inteligência Artificial (IA) e Aprendizado de Máquina",
        "local": "Campo Grande",
        "participantes": {'07610192198':
                {'Nome': 'Vinicius henrique de souza lima',
                 'Email': 'Vinisk8.cba@gmail.com',
                 'Preferencias Tematicas': 'Tech'}}
    },
    {
        "nome": "Summer day",
        "data": "11-05-2025",
        "tema": "Big Data e Analytics",
        "local": "Rio de Janeiro",
        "participantes": {'07610192198':
                {'Nome': 'Vinicius henrique de souza lima',
                 'Email': 'Vinisk8.cba@gmail.com',
                 'Preferencias Tematicas': 'Tech'}}
    } 
]

def listar_eve():
    for i, evento in enumerate(eve):
        print(f"{i}. {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Participantes: {len(evento['participantes'])}")


eventos = [{ 
        'Python Day': {'Data': '01-12-2025',
        'Tema': 'Segurança Cibernética',
        'Local': 'São Paulo',
        'Participantes': {'07610192198': {'Nome': 'Vinicius henrique de souza lima', 'Email': 'Vinisk8.cba@gmail.com', 'Preferencias Tematicas': 'Tech'}}}
    }]

def listar_eventos():
    for i, evento in enumerate(eventos):
        for nome, dados in evento.items():
            # print(f"Evento {i} : {nome} | Data: {j['Data']} | Tema: {j['Tema']} | Local: {j['Local']} | Participantes: {len(j['Participantes'])}")
            pass