from marshmallow import fields
from ..config.db import db
from ..config.ma import ma


class Bloque(db.Model):
    __tablename__ = 'bloque'
    id_edificio = db.Column(db.String(25), primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    piso = db.Column(db.Integer, nullable=False)
    salon = db.relationship('Salon')
     
    def __repr__(self):
        return '<Bloque %r>' % self.id_edificio % self.nombre %self.piso

class BloqueSchema(ma.Schema):
    class Meta:
        fields = ('id_edificio', 'nombre', 'piso')

bloque_schema = BloqueSchema()
bloques_schema = BloqueSchema(many=True)