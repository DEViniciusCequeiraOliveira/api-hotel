class HotelModel:
    def __init__(self, hotel_id, nome, estrela, cidade, diaria):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrela = estrela
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
        'hotel_id': self.hotel_id,
        'nome': self.nome,
        'cidade': self.cidade,
        'estrela': self.estrela,
        'diaria': self.diaria
    }
