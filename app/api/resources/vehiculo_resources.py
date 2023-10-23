from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.vehiculo_models import Vehiculo
from ..schemas.vehiculo_schemas import VehiculoSchema

api_usuario = Api(api)

class VehiculoResource(Resource):
    
    def get(self):
        data = Vehiculo.get_all()
        schema = VehiculoSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de Vehiculos',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            vehiculo = Vehiculo()
            vehiculo.placa = data['placa']
            vehiculo.conductor= data['conductor']
            vehiculo.save()
            
            schema = VehiculoSchema()
            return {
                'status':True,
                'content':schema.dump(vehiculo)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':'Es una excepcion'+str(e.args)
            },500
            
class VehiculoDetailResource(Resource):
    
    def get(self,id):
        vehiculo = Vehiculo.get_by_id(id)
        schema = VehiculoSchema()
        context = {
            'status':True,
            'content':schema.dump(vehiculo)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        placa = data['placa']
        conductor = data['conductor']
       
        
        vehiculo = Vehiculo.get_by_id(id)
        vehiculo.placa = placa        
        vehiculo.conductor = conductor
        vehiculo.save()
        
        schema =VehiculoSchema()
        
        context = {
            'status':True,
            'content':schema.dump(vehiculo)
        }
        
        return context
    
    def delete(self,id):
        vehiculo = Vehiculo.get_by_id(id)
        vehiculo.delete()
        
        schema = VehiculoSchema()
        
        context = {
            'status':True,
            'content':schema.dump(vehiculo)
        }
        
        return context
            

    
api_usuario.add_resource(VehiculoResource,'/vehiculo')
api_usuario.add_resource(VehiculoDetailResource,'/vehiculo/<id>')