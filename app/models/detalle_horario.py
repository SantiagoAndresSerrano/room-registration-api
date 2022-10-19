from marshmallow import fields
from ..models.grupo_materia import GrupoMateriaSchema
from ..models.horario import HorarioSchema
from ..config.db import db
from ..config.ma import ma


class DetalleHorario(db.Model):
    __tablename__ = 'detalle_horario'
    id_det_hor = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.Integer, db.ForeignKey('horario.id_horario'))
    grupo_materia = db.Column(db.Integer, db.ForeignKey('grupo_materia.id_grup_mat'))
    horarioRel: db.relationship('Horario', back_populates="detallle_horario")
    grupo_materiaRel: db.relationship('GrupoMateria', back_populates="detallle_horario")

class DetalleHorarioSchema(ma.Schema):
    class Meta:
        fields = ('id_grup_mat','horarioRel', 'grupo_materiaRel')
    horarioRel = fields.Nested(HorarioSchema(only=('id_horario', 'hora_inicio','hora_final')))
    grupo_materiaRel = fields.Nested(GrupoMateriaSchema(only=('id_grup_mat','periodo', 'cupos', 'grupoRel', 'materiaRel')))
    
det_horario_schema = DetalleHorarioSchema()
dets_horario_schema = DetalleHorarioSchema(many=True)