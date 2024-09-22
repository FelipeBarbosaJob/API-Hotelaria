from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):

    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' é obrigatório.")
    atributos.add_argument('estrelas', type=float, required=True, help="O campo 'estrelas' é obrigatório.")
    atributos.add_argument('diaria', type=float, required=True, help="O campo 'diaria' é obrigatório.")
    atributos.add_argument('cidade', type=str, required=True, help="O campo 'cidade' é obrigatório.")
  
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()

        return {'message': 'Hotel não encontrado.'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': 'Hotel id {} já existe.'.format(hotel_id)}, 400
        
        else:
            dados = Hotel.atributos.parse_args()
            hotel = HotelModel(hotel_id, **dados)
            try:
                hotel.save_hotel()
            except:
                return {'message': 'ERRO TENTANDO SALVAR HOTEL'},500
            return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)
    
        if hotel_encontrado:
            
            hotel_encontrado.update_hotel(**dados)  # Atualiza os dados
            hotel_encontrado.save_hotel()  # Salva no banco
            return hotel_encontrado.json(), 200  
        else:
            hotel = HotelModel(hotel_id, **dados)
            try:
                    hotel.save_hotel()
            except:
                    return {'message': 'ERRO TENTANDO SALVAR HOTEL'},500
            return hotel.json(), 201
        
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'ERRO TENTANDO DELETAR HOTEL'},500
            return {'message': 'Hotel deletado.'}, 200
        else:
            return {'message': 'Hotel não existe.'}, 404
        
        
        