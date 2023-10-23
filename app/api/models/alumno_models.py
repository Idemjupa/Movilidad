from utils import db

class Alumno(db.Model):
    __tablename__ = 'tbl_alumno'
    
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255),nullable=True)
    apellido = db.Column(db.String(200),nullable=True)
    fecha_nacimiento = db.Column(db.Date,nullable=True)
    foto = db.Column(db.Text,nullable=False)
    
    @staticmethod
    def get_all():
        return Alumno.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Alumno.query.get(id)
    
    @staticmethod
    def get_by_email(nombre):
        return Alumno.query.filter_by(nombre=nombre).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()