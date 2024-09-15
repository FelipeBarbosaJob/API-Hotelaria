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

    # Cria um parser para os dados do hotel
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id): # para fazer a busca de hoteis se existe ou não
        # Busca um hotel específico pelo ID e retorna seus dados em formato JSON
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel

        # Retorna uma mensagem de erro se o hotel não for encontrado
        return {'message': 'Hotel não encontrado.'}, 404

    def post(self, hotel_id):

        
        dados = Hotel.argumentos.parse_args()
        novo_hotel = { 'hotel_id': hotel_id, **dados } # Adiciona o novo hotel à lista

        hoteis.append(novo_hotel) #append = adicionar um novo elemento a lista
        return novo_hotel, 200
    
    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        novo_hotel = { 'hotel_id': hotel_id, **dados }

        hotel = Hotel.find_hotel(hotel_id)
        if hotel: #atualiza um hotel existente
            hotel.update(novo_hotel)
            return novo_hotel, 200
        
        hoteis.append(novo_hotel) #cria um novo hotel
        return novo_hotel,201


    def delete(self, hotel_id):
        pass
