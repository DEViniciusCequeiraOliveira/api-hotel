from flask_restful import Resource, reqparse
from models.hotel import HotelModel
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

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrela')
    argumentos.add_argument('cidade')
    argumentos.add_argument('diaria')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    # ler informações de determinado hotel
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message' : "Não encontrado"}, 404

    # criar um novo
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    # editar
    def put(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        dados = Hotel.argumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        if hotel:
            hotel.update(novo_hotel)
            return hotel, 200
        hoteis.append(novo_hotel)
        return hotel, 201 # created

    # apagar
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message' : 'Hotel deleted.'}
        pass