from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.movilidad_models import Movilidad
from ..schemas.movilidad_schema import MovilidadSchema

api_usuario = Api(api)

class MovilidadResource(Resource):
    
    def get(self):
        data = Movilidad.get_all()
        schema = MovilidadSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de Movilidades',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            movilidad = Movilidad()
            movilidad.tipo_servicio = data['tipo_servicio']
            movilidad.turno = data['turno']
            movilidad.seccion = data['seccion']
            movilidad.docente = data['docente']
            movilidad.pago = data['pago']
            movilidad.colegio_id = data['colegio_id']
            movilidad.vehiculo_id = data['vehiculo_id']
            movilidad.alumno_id = data['alumno_id']
            movilidad.save()
            
            schema = MovilidadSchema()
            return {
                'status':True,
                'content':schema.dump(movilidad)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':'Es una excepcion'+str(e.args)
            },500
            
class MovilidadDetailResource(Resource):
    
    def get(self,id):
        movilidad = Movilidad.get_by_id(id)
        schema = MovilidadSchema()
        context = {
            'status':True,
            'content':schema.dump(movilidad)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        tipo_servicio = data['tipo_servicio']
        turno = data['turno']
        seccion = data['seccion']
        docente = data['docente']
        pago = data['pago']
        colegio_id = data['colegio_id']
        vehiculo_id = data['vehiculo_id']
        alumno_id = data['alumno_id']
          
        
        movilidad = Movilidad.get_by_id(id)
        movilidad.tipo_servicio = tipo_servicio
        movilidad.turno = turno
        movilidad.seccion =seccion
        movilidad.docente = docente
        movilidad.pago = pago
        movilidad.colegio_id =colegio_id
        movilidad.vehiculo_id = vehiculo_id
        movilidad.alumno_id = alumno_id
        movilidad.save()
        
        schema =MovilidadSchema()
        
        context = {
            'status':True,
            'content':schema.dump(movilidad)
        }
        
        return context
    
    def delete(self,id):
        movilidad = Movilidad.get_by_id(id)
        movilidad.delete()
        
        schema = MovilidadSchema()
        
        context = {
            'status':True,
            'content':schema.dump(movilidad)
        }
        
        return context
            

    
api_usuario.add_resource(MovilidadResource,'/movilidad')
api_usuario.add_resource(MovilidadDetailResource,'/movilidad/<id>')