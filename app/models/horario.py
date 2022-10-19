from sqlalchemy import DateTime
from sqlalchemy.sql import func
from marshmallow import fields
from ..config.db import db
from ..config.ma import ma


class Horario(db.Model):
    __tablename__ = 'horario'
    id_horario = db.Column(db.String(1), primary_key=True)
    hora_inicio = db.Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    hora_final = db.Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    detalle_horario: db.relationship('DetalleHorario', back_populates="horarioRel")
     
    def __repr__(self):
        return '<Horario %r>' % self.id_horario % self.hora_inicio & self.hora_Final

class HorarioSchema(ma.Schema):
    class Meta:
        fields = ('id_horario', 'hora_inicio','hora_final')

horario_schema = HorarioSchema()
horarios_schema = HorarioSchema(many=True)