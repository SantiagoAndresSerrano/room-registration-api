from marshmallow import fields

from ..models.salon import SalonSchema
from ..models.tipo_inventario import TipoInventarioSchema
from ..config.db import db
from ..config.ma import ma

# # from ..models.salon import SalonSchema
# from ..models.tipo_inventario import TipoInventarioSchema
# from ..models.tipo_inventario import tiposInven_schema, tipoInven_schema

class DetalleInventario(db.Model):
    __tablename__ = 'detalle_inventario'
    id_detalle = db.Column(db.Integer, primary_key=True)
    # cantidad = db.Column(db.Integer)
    salon = db.Column(db.String(10), db.ForeignKey('salon.id_salon'))
    tipo_inventario = db.Column(db.Integer, db.ForeignKey('tipo_inventario.id_tipo'))
    salonRel = db.relationship('Salon')
    tipoRel = db.relationship('TipoInventario')
     

class DetalleInventarioSchema(ma.Schema):
    class Meta:
        fields = ('id_detalle','salon', 'tipoRel')
    # salonRel = fields.Nested(SalonSchema(only=('id_salon', 'tipo', 'estado', 'cupo', 'bloqueRel','grupo_materiaRel')))
    tipoRel = fields.Nested(TipoInventarioSchema(only=(('id_tipo', 'nombre', 'descripcion'))))


detalleInven_schema = DetalleInventarioSchema()
detallesInven_schema = DetalleInventarioSchema(many=True)