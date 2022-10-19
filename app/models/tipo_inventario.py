from marshmallow import fields
from ..config.db import db

from ..config.ma import ma


class TipoInventario(db.Model): 
    __tablename__ = 'tipo_inventario'
    id_tipo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    detalles = 'detalle_inventario',db.relationship('DetalleInventario', back_populates="tipo_inventario")
     
    def __repr__(self):
        return '<TipoInventario %r>' % self.id_tipo % self.nombre %self.descripcion
 
class TipoInventarioSchema(ma.Schema):
    class Meta:
        fields = ('id_tipo', 'nombre', 'descripcion')

tipoInven_schema = TipoInventarioSchema()
tiposInven_schema = TipoInventarioSchema(many=True)