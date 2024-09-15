from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis

# Criação da instância do aplicativo Flask
app = Flask(__name__)
# Criação da instância da API Flask-RESTful
api = Api(app)

# Associa a classe Hoteis ao endpoint /hoteis
api.add_resource(Hoteis, '/hoteis')

# Executa o aplicativo Flask apenas se o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Executa o servidor Flask em modo de depuração

    # O servidor pode ser acessado em http://127.0.0.1:5000/hoteis
