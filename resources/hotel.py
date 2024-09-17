from flask_restful import Resource, reqparse
from models.hotel import HotelModel

# Lista de hotéis em formato JSON. Aqui simulamos um banco de dados de hotéis com algumas entradas iniciais.
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



# Classe 'Hoteis', que gerencia o endpoint /hoteis e retorna a lista de todos os hotéis.
class Hoteis(Resource):
    def get(self):
        # Retorna a lista de todos os hotéis disponíveis no formato JSON.
        return {'hoteis': hoteis}

# Classe 'Hotel', que gerencia as operações em um hotel específico baseado no 'hotel_id'.
class Hotel(Resource):

    # Criação de um parser para definir os argumentos que serão aceitos nas requisições.
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')      # Argumento para o nome do hotel
    argumentos.add_argument('estrelas')   # Argumento para a quantidade de estrelas do hotel
    argumentos.add_argument('diaria')     # Argumento para o valor da diária do hotel
    argumentos.add_argument('cidade')     # Argumento para a cidade onde o hotel está localizado

    # Função auxiliar que busca um hotel específico pelo 'hotel_id'. Retorna o hotel se encontrado ou None se não.
    @staticmethod
    def find_hotel(hotel_id):
        # Itera pela lista de hotéis e compara o 'hotel_id' para encontrar o hotel.
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        # Retorna None se o hotel com o 'hotel_id' fornecido não for encontrado.
        return None

    # Método GET: Busca um hotel específico pelo 'hotel_id' e retorna seus dados, ou uma mensagem de erro se não encontrado.
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            # Se o hotel for encontrado, retorna seus dados no formato JSON.
            return hotel

        # Se o hotel não for encontrado, retorna uma mensagem de erro com status 404 (Not Found).
        return {'message': 'Hotel não encontrado.'}, 404

    # Método POST: Cria um novo hotel com base no 'hotel_id' fornecido e nos dados enviados na requisição.
    def post(self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
        # Se o hotel for encontrado, retorna seus dados no formato JSON.
            return {'message': 'Hotel hotel já existe.'}, 404
        # Faz o parsing dos argumentos recebidos e cria um novo dicionário 'novo_hotel'.
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        # Adiciona o novo hotel à lista de hotéis.
        hoteis.append(novo_hotel)
        
        # Retorna o novo hotel criado e o status 201 (Created).
        return novo_hotel, 201
    
    # Método PUT: Atualiza os dados de um hotel existente ou cria um novo hotel caso o 'hotel_id' não exista.
    def put(self, hotel_id):
        # Faz o parsing dos argumentos recebidos e cria um dicionário 'novo_hotel' com os dados.
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()

        # Procura o hotel pelo 'hotel_id'.
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:  # Se o hotel for encontrado, atualiza os dados.
            hotel.update(novo_hotel)  # O método update substitui os valores existentes pelos novos dados.
            return novo_hotel, 200  # Retorna o hotel atualizado com status 200 (OK).
        
        else:
            hoteis.append(novo_hotel)# Se o hotel não for encontrado, adiciona um novo hotel à lista de hotéis.
            return novo_hotel, 201# Retorna o novo hotel criado com status 201 (Created).

    def delete(self, hotel_id):
        # Busca o hotel pelo ID para verificar se ele existe
        hotel = Hotel.find_hotel(hotel_id)
        
        # Se o hotel não for encontrado, retorna um erro
        if hotel is None:
            return {'message': 'Hotel não existe.'}, 404
        
        # Remove o hotel da lista filtrando por IDs diferentes do ID passado
        hoteis[:] = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id] 
        return {'message': 'Hotel deleted.'}, 200
        