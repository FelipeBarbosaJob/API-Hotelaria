from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel  # Importa os recursos Hoteis e Hotel do módulo resources.hotel

app = Flask(__name__) # Criação da instância do aplicativo Flask

api = Api(app) # Criação da instância da API Flask-RESTful


api.add_resource(Hoteis, '/hoteis') # Associa a classe Hoteis ao endpoint /hoteis

api.add_resource(Hotel, '/hoteis/<string:hotel_id>')# Associa a classe Hotel ao endpoint /hoteis/<string:hotel_id>
                                                    # Esse endpoint permite acessar informações de um hotel específico por ID


if __name__ == '__main__': # Executa o aplicativo Flask apenas se o script for executado diretamente

    app.run(debug=True)  # Executa o servidor Flask em modo de depuração

    # O servidor pode ser acessado em http://127.0.0.1:5000/hoteis

