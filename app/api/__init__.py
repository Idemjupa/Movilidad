from flask import Blueprint,jsonify

api = Blueprint('api',__name__,url_prefix='/api')

from .resources import (
    usuario_resources,
    alumno_resources,
    colegio_resources,
    vehiculo_resources,
    movilidad_resources
)

@api.route('/')
def index():
    context ={
        'message':'blueprint api'
    }
    return jsonify(context)