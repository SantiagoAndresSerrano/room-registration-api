from marshmallow import fields
from ..models.grupo import GrupoSchema
from ..models.materia import MateriaSchema
from ..config.db import db
from ..config.ma import ma
class GrupoMateria(db.Model):
    __tablename__ = 'grupo_materia'
    id_grup_mat = db.Column(db.Integer, primary_key=True)
    periodo = db.Column(db.String(25), nullable=False)
    cupos = db.Column(db.Integer, nullable=False)
    grupo = db.Column(db.String(1), db.ForeignKey('grupo.id_grupo'))
    materia = db.Column(db.Integer, db.ForeignKey('materia.id_materia'))
    grupoRel= db.relationship('Grupo', back_populates="grupo_materia")
    materiaRel= db.relationship('Materia')
    detalle_horario=db.relationship('DetalleHorario', back_populates="grupo_materiaRel")
    salon=db.relationship('Salon')

class GrupoMateriaSchema(ma.Schema):
    class Meta:
        fields = ('id_grup_mat','periodo', 'cupos', 'grupoRel', 'materiaRel')
    grupoRel = fields.Nested(GrupoSchema(only=('id_grupo', 'estado')))
    materiaRel = fields.Nested(MateriaSchema(only=('id_materia', 'nombre')))
    
grupo_materia_schema = GrupoMateriaSchema()
grupos_materia_schema = GrupoMateriaSchema(many=True)