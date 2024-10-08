from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel  
from resources.usuario import Usuarios, User, UserRegistrer



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/felip/OneDrive/Documentos/Projetos/REST_API/banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegistrer, '/cadastro')
if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)  # Inicia o servidor


    # O servidor pode ser acessado em http://127.0.0.1:5000/hoteis

