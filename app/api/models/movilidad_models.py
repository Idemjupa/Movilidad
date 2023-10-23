from utils import db

class Movilidad(db.Model):
    __tablename__ = 'tbl_movilidad'
    
    id = db.Column(db.Integer,primary_key=True)
    tipo_servicio = db.Column(db.String(255),nullable=False)
    turno = db.Column(db.String(255),nullable=False)
    seccion = db.Column(db.String(255),nullable=False)
    docente = db.Column(db.String(255),nullable=False)
    pago = db.Column(db.Double,nullable=False)
    colegio_id = db.Column(db.Integer,nullable=False)
    vehiculo_id = db.Column(db.Integer,nullable=False)
    alumno_id = db.Column(db.Integer,nullable=False)

    
    @staticmethod
    def get_all():
        return Movilidad.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Movilidad.query.get(id)
       
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()