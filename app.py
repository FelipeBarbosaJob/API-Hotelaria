from flask import Flask
from flask_restful import Resource, Api

# Criação da instância do aplicativo Flask
app = Flask(__name__)
# Criação da instância da API Flask-RESTful
api = Api(app)

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

# Definição da classe Hoteis, que irá gerenciar o endpoint /hoteis
class Hoteis(Resource): 
    def get(self):
        # Retorna a lista de hotéis em formato JSON
        return {'hoteis': hoteis}

# Associa a classe Hoteis ao endpoint /hoteis
api.add_resource(Hoteis, '/hoteis')

# Executa o aplicativo Flask apenas se o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Executa o servidor Flask em modo de depuração

    # O servidor pode ser acessado em http://127.0.0.1:5000/hoteis
