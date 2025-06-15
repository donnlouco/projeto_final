eve = [
    {
        "nome": "Python Day",
        "data": "2025-07-01",
        "local": "São Paulo",
        "participantes": []
    },
    {
        "nome": "Tech Summit",
        "data": "2025-08-15",
        "local": "Rio de Janeiro",
        "participantes": []
    },
    {
        "nome": "Autumn Day",
        "data": "2025-07-01",
        "local": "São Paulo",
        "participantes": []
    },
    {
        "nome": "Summer day",
        "data": "2025-08-15",
        "local": "Rio de Janeiro",
        "participantes": []
    } 
]

def listar_eve():
    for i, evento in enumerate(eve):
        print(f"{i}. {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Participantes: {len(evento['participantes'])}")

