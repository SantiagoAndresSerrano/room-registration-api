from marshmallow import fields

from ..models.grupo_materia import GrupoMateriaSchema
from ..config.db import db
from ..config.ma import ma
from .bloque import BloqueSchema


class Salon(db.Model):
    __tablename__ = 'salon'
    id_salon = db.Column(db.String(10), primary_key=True)
    tipo = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    cupo = db.Column(db.Integer, nullable=False)
    grupo_materia = db.Column(db.Integer, db.ForeignKey('grupo_materia.id_grup_mat'))
    bloque = db.Column(db.String(25), db.ForeignKey('bloque.id_edificio'))
    bloqueRel= db.relationship('Bloque', back_populates="salon")
    grupo_materiaRel: db.relationship('GrupoMateria', back_populates="salonRel")
    detalle_inventario: db.relationship('DetalleInventario', back_populates="salonRel")

    def __repr__(self):
        return '<Salon %r>' % self.id_salon % self.tipo %self.estado

class SalonSchema(ma.Schema):
    class Meta:
        fields = ('id_salon', 'tipo', 'estado', 'cupo', 'bloqueRel', 'grupo_materiaRel')
    bloqueRel = fields.Nested(BloqueSchema(only=(('id_edificio', 'nombre', 'piso'))))
    grupo_materiaRel = fields.Nested(GrupoMateriaSchema(only=('id_grup_mat','periodo', 'cupos', 'grupoRel', 'materiaRel')))
    

salon_schema = SalonSchema()
salones_schema = SalonSchema(many=True)
    