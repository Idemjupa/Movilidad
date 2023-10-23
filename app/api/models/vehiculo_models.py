from utils import db

class Vehiculo(db.Model):
    __tablename__ = 'tbl_vehiculo'
    
    id = db.Column(db.Integer,primary_key=True)
    placa = db.Column(db.String(255),nullable=False)
    conductor = db.Column(db.String(255),nullable=False)
    
    @staticmethod
    def get_all():
        return Vehiculo.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Vehiculo.query.get(id)
    
    @staticmethod
    def get_by_placa(placa):
        return Vehiculo.query.filter_by(placa=placa).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()