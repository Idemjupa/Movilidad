from utils import ma

class ColegioSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre')