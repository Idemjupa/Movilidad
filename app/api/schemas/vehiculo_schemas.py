from utils import ma

class VehiculoSchema(ma.Schema):
    class Meta:
        fields = ('id','placa','conductor')