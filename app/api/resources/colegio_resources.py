from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.colegio_models import Colegio
from ..schemas.colegio_schemas import ColegioSchema

api_usuario = Api(api)

class ColegioResource(Resource):
    
    def get(self):
        data = Colegio.get_all()
        schema = ColegioSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de Colegios',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            colegio = Colegio()
            colegio.nombre = data['nombre']
            colegio.save()
            
            schema = ColegioSchema()
            return {
                'status':True,
                'content':schema.dump(colegio)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':'Es una excepcion'+str(e.args)
            },500
            
class ColegioDetailResource(Resource):
    
    def get(self,id):
        colegio = Colegio.get_by_id(id)
        schema = ColegioSchema()
        context = {
            'status':True,
            'content':schema.dump(colegio)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        nombre = data['nombre']
       
        
        colegio = Colegio.get_by_id(id)
        colegio.nombre = nombre        
        colegio.save()
        
        schema =ColegioSchema()
        
        context = {
            'status':True,
            'content':schema.dump(colegio)
        }
        
        return context
    
    def delete(self,id):
        colegio = Colegio.get_by_id(id)
        colegio.delete()
        
        schema = ColegioSchema()
        
        context = {
            'status':True,
            'content':schema.dump(colegio)
        }
        
        return context
            

    
api_usuario.add_resource(ColegioResource,'/colegio')
api_usuario.add_resource(ColegioDetailResource,'/colegio/<id>')