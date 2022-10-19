from marshmallow import fields
from ..config.db import db
from ..config.ma import ma


class Grupo(db.Model):
    __tablename__ = 'grupo'
    id_grupo = db.Column(db.String(1), primary_key=True)
    estado = db.Column(db.Integer, nullable=False)
    grupo_materia = db.relationship('GrupoMateria')
     
    def __repr__(self):
        return '<Grupo %r>' % self.id_grupo % self.estado

class GrupoSchema(ma.Schema):
    class Meta:
        fields = ('id_grupo', 'estado')

grupo_schema = GrupoSchema()
grupos_schema = GrupoSchema(many=True)