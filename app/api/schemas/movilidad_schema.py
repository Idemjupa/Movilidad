from utils import ma

class MovilidadSchema(ma.Schema):
    class Meta:
        fields=('id','tipo_servicio','turno' ,'seccion','docente','pago' ,'colegio_id' ,'vehiculo_id','alumno_id')