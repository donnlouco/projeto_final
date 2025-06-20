eve = [
    {
        "nome": "Python Day",
        "data": "2025-07-01",
        "tema": "Segurança Cibernética",
        "local": "São Paulo",
        "participantes": {}
    },
    {
        "nome": "Tech Summit",
        "data": "2025-08-15",
        "tema": "Transformação Digital",
        "local": "Rio de Janeiro",
        "participantes":  {}
    },
    {
        "nome": "Autumn Day",
        "data": "2025-07-01",
        "tema": "Inteligência Artificial (IA) e Aprendizado de Máquina",
        "local": "São Paulo",
        "participantes": {}
    },
    {
        "nome": "Summer day",
        "data": "2025-08-15",
        "tema": "Big Data e Analytics",
        "local": "Rio de Janeiro",
        "participantes": {}
    } 
]

def listar_eve():
    for i, evento in enumerate(eve):
        print(f"{i}. {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Participantes: {len(evento['participantes'])}")




