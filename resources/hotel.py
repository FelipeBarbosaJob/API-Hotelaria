from flask_restful import Resource, reqparse

# Lista de hotéis em formato JSON
hoteis = [
    {
        "hotel_id": "101",
        "nome": "Hotel Paraíso",
        "estrelas": 5,
        "diaria": 350.00,
        "cidade": "Rio de Janeiro"
    },
    {
        "hotel_id": "102",
        "nome": "Pousada do Sol",
        "estrelas": 4,
        "diaria": 250.00,
        "cidade": "Salvador"
    },
    {
        "hotel_id": "103",
        "nome": "Resort Mar Azul",
        "estrelas": 5,
        "diaria": 500.00,
        "cidade": "Florianópolis"
    },
    {
        "hotel_id": "104",
        "nome": "Hotel Central",
        "estrelas": 3,
        "diaria": 150.00,
        "cidade": "São Paulo"
    },
    {
        "hotel_id": "105",
        "nome": "Pousada Montanha",
        "estrelas": 4,
        "diaria": 200.00,
        "cidade": "Belo Horizonte"
    }
]

# Definição da classe Hoteis, que gerencia o endpoint /hoteis
class Hoteis(Resource):
    def get(self):
        # Retorna a lista de todos os hotéis em formato JSON
        return {'hoteis': hoteis}

# Definição da classe Hotel, que gerencia o endpoint /hoteis/<string:hotel_id>
class Hotel(Resource):
    def get(self, hotel_id):
        # Busca um hotel específico pelo ID e retorna seus dados em formato JSON
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        # Retorna uma mensagem de erro se o hotel não for encontrado
        return {'message': 'Hotel não encontrado.'}, 404

    def post(self, hotel_id):

        # Cria um parser para os dados do hotel
        argumento = reqparse.RequestParser()
        argumento.add_argument('nome')
        argumento.add_argument('estrelas')
        argumento.add_argument('diaria')
        argumento.add_argument('cidade')
        args = argumento.parse_args()

        # Adiciona o novo hotel à lista
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': args['nome'],
            'estrelas': args['estrelas'],
            'diaria': args['diaria'],
            'cidade': args['cidade']
        }
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
