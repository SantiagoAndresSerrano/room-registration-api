from flask import Blueprint, request
from flask_api import status
from app.models.detalle_inventario import DetalleInventarioSchema
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

from ..models.tipo_inventario import TipoInventario
from ..models.tipo_inventario import tipoInven_schema, tiposInven_schema
from ..models.detalle_inventario import DetalleInventario, detalleInven_schema, detallesInven_schema


inventario = Blueprint("inventario",__name__)

    
#Retorna todos los detalles de los inventarios
@inventario.route("/roomregister/salon/inventario/detalleinventario/", methods=["GET"])
@cross_origin()
def getDetalleinventario():
    """Retorna el detalle de todos los elementos de un salón
    ---
    tags:
      - Inventario
    definitions:
        Inventario:
          type: object
          properties:
              id_detalle:
                type: integer
              tipoRel:
                type: object
                properties:
                    id_tipo: 
                        type: integer
                    nombre: 
                        type: string
                    descripcion: 
                        type: string
              salonRel:
                type: object
                properties:
                  id_salon:
                    type: string
                  tipo:
                    type: integer
                  estado:
                    type: integer
                  cupo:
                    type: integer
                  BloqueRel:
                    type: object
                    properties:
                      id_edificio:
                        type: string
                      nombre:
                        type: string
                      piso:
                        type: integer

    responses:
      200:
        description: Lista de detalle en el inventario del salón
        schema:
          $ref: '#/definitions/Inventario'
    """
    try:
        allDetalles = DetalleInventario.query.all()
        return detallesInven_schema.dump(allDetalles), status.HTTP_200_OK
    except NoResultFound:
        return "Detalles inventario not found", status.HTTP_401_UNAUTHORIZED

#Retorna todos los detalles de los inventarios
@inventario.route("/roomregister/inventario/<string:id_salon>", methods=["GET"])
@cross_origin()
def getDetalleinventarioSalon(id_salon):
    """Retorna el detalle de todos los elementos de un salón
    ---
    tags:
      - Inventario
    parameters:
      - name: id_salon
        in: path
        type: string
        required: true
        description: Identifier salon, example (SA401)
    responses:
      200:
        description: Lista de detalle en el inventario del salón
        schema:
          $ref: '#/definitions/Inventario'
    """
    try:
        allDetalles = DetalleInventario.query.filter(DetalleInventario.salon == id_salon)
        return detallesInven_schema.dump(allDetalles), status.HTTP_200_OK
    except NoResultFound:
        return "Detalles inventario not found", status.HTTP_401_UNAUTHORIZED

##Returns all tipos de elementos de un salón
@inventario.route("/roomregister/salon/inventario/tipos/" , methods=["GET"])
@cross_origin()
def getAllTipoInventario():
    """Retorna una lista de tipos de elementos en un salón
    ---
    tags:
      - Salon
    definitions:
        Tipo:
          type: object
          properties:
            id_tipo: 
                type: integer
            nombre: 
                type: string
            descripcion: 
                type: string
              
    responses:
      200:
        description: Lista de tipos de elementos del salón
        schema:
          $ref: '#/definitions/Tipo'
    """
    try:
        all_tipos = TipoInventario.query.all()
        return tiposInven_schema.dump(all_tipos), status.HTTP_200_OK
    except NoResultFound:
        return "Tipo de inventario not found", status.HTTP_401_UNAUTHORIZED
    
##Retorna los elementos de un determinado salón


##Editar el estado de un determinado elemento de un salón 
