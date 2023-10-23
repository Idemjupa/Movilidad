from utils import ma

class AlumnoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','apellido','fecha_nacimiento','foto')