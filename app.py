from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel  
from sql_alchemy import banco
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/felip/OneDrive/Documentos/Projetos/REST_API/banco.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app) 


api.add_resource(Hoteis, '/hoteis')

api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__ == '__main__': 
    
    banco.init_app(app)
    with app.app_context():
        banco.create_all()

    app.run(debug=True)  

    # O servidor pode ser acessado em http://127.0.0.1:5000/hoteis

