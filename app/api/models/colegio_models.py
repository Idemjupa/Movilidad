from utils import db

class Colegio(db.Model):
    __tablename__ = 'tbl_colegio'
    
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255),nullable=False)
    
    @staticmethod
    def get_all():
        return Colegio.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Colegio.query.get(id)
    
    @staticmethod
    def get_by_email(nombre):
        return Colegio.query.filter_by(nombre=nombre).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()