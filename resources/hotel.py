from flask_restful import Resource

hoteis = [
    {
        'hotel_id' : 'alpha',
        'nome' : 'Alpha Hotel',
        'cidade' : 'Feira de Santana',
        'estrela' : 4.3,
        'diaria' : 450.15
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'cidade': 'Serrinha',
        'estrela': 3.3,
        'diaria': 270.32
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'cidade': 'Salvador',
        'estrela': 2.7,
        'diaria': 650.82
    },
    {
        'hotel_id': 'delta',
        'nome': 'Delta Hotel',
        'cidade': 'Camaçari',
        'estrela': 4.7,
        'diaria': 300.00
    },
]

class Hoteis(Resource):
    # ler informações
    def get(self):
        return {'hoteis' : hoteis}
