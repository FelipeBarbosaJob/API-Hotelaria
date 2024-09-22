from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token



atribitos = reqparse.RequestParser()
atribitos.add_argument('login', type=str, required=True, help="O campo 'login' não pode ficar em branco.")
atribitos.add_argument('senha', type=str, required=True, help="O campo 'login' não pode ficar em branco.")

class Usuarios(Resource):
    def get(self):
        return {'usuarios': [user.json() for user in UserModel.query.all()]}

class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()

        return {'message': 'Usuario não encontrado.'}, 404
    
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'ERRO TENTANDO DELETAR USUARIO'},500
            return {'message': 'Usuario deletado.'}, 200
        else:
            return {'message': 'Usuario não existe.'}, 404
        
class UserRegistrer(Resource):

    def post(self):
        dados = atribitos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": " Usuario '{}'.".format(dados['login'])}, 200
        
        user = UserModel(**dados)
        user.save_user()
        return {"message": " Usuario '{}'. criado com sucesso".format(dados['login'])}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atribitos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identify=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'Usuario ou Senha está incorreta'}, 401







