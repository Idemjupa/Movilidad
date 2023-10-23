from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.alumno_models import Alumno
from ..schemas.alumno_schemas import AlumnoSchema

api_usuario = Api(api)

class AlumnoResource(Resource):
    
    def get(self):
        data = Alumno.get_all()
        schema = AlumnoSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de alumnos',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            alumno = Alumno()
            alumno.nombre = data['nombre']
            alumno.apellido = data['apellido']
            alumno.fecha_nacimiento = data['fecha_nacimiento']
            alumno.foto = data['foto']
            alumno.save()
            
            schema = AlumnoSchema()
            return {
                'status':True,
                'content':schema.dump(alumno)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':'Es una excepcion'+str(e.args)
            },500
            
class AlumnoDetailResource(Resource):
    
    def get(self,id):
        alumno = Alumno.get_by_id(id)
        schema = AlumnoSchema()
        context = {
            'status':True,
            'content':schema.dump(alumno)
        }
        
        return context
    
    def put(self,id):
        data = request.get_json()
        nombre = data['nombre']
        apellido = data['apellido']
        fecha_nacimiento = data['fecha_nacimiento']
        foto = data['foto']
        
        
        alumno = Alumno.get_by_id(id)
        alumno.nombre = nombre
        alumno.apellido = apellido
        alumno.fecha_nacimiento= fecha_nacimiento
        alumno.save()
        
        schema =AlumnoSchema()
        
        context = {
            'status':True,
            'content':schema.dump(alumno)
        }
        
        return context
    
    def delete(self,id):
        alumno = Alumno.get_by_id(id)
        alumno.delete()
        
        schema = AlumnoSchema()
        
        context = {
            'status':True,
            'content':schema.dump(alumno)
        }
        
        return context
            

    
api_usuario.add_resource(AlumnoResource,'/alumno')
api_usuario.add_resource(AlumnoDetailResource,'/alumno/<id>')