from marshmallow import fields
from ..config.db import db
from ..config.ma import ma


class Materia(db.Model):
    __tablename__ = 'materia'
    id_materia = db.Column(db.String(1), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    grupo_materia = db.relationship('GrupoMateria')
     
    def __repr__(self):
        return '<Materia %r>' % self.id_materia % self.nombre

class MateriaSchema(ma.Schema):
    class Meta:
        fields = ('id_materia', 'nombre')

materia_schema = MateriaSchema()
materias_schema = MateriaSchema(many=True)