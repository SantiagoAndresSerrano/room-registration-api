from flask import Blueprint, request
from flask_api import status
from ..models.salon import Salon
from ..models.salon import salon_schema, salones_schema
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

salones = Blueprint("salones",__name__)

@salones.route("/roomregister/salon" , methods=["GET"])
@cross_origin()
def getAllSalones():
    """Retorna todos los salones
    ---
    tags:
      - Salon
    definitions:
      Salon:
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
        description: A list of rooms
        schema:
          $ref: '#/definitions/Salon'
    """
    try:
        all_salones = Salon.query.all()
        return salones_schema.dump(all_salones), status.HTTP_200_OK
    except NoResultFound:
        return "Salones not found", status.HTTP_401_UNAUTHORIZED

##Encontrar un salón
@salones.route("/roomregister/salon/<string:id_salon>", methods=["GET"])
@cross_origin()
def encontrarSalon(id_salon):
    """Retorna la información del salón a encontrar
      ---
      tags:
        - Salon
      parameters:
        - name: id_salon
          in: path
          type: string
          required: true
          description: Identifier salon
      definitions:
        Salon:
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
          description: A room class
          schema:
            $ref: '#/definitions/Salon'
      """
    try:
        salonFound = Salon.query.filter(Salon.id_salon == id_salon).one()
    except NoResultFound:
        return "Salon not found", status.HTTP_401_UNAUTHORIZED
    return salon_schema.dump(salonFound), status.HTTP_200_OK

##Editar el estado de un determinado salón 
# @salones.route("/salon/<string:salon>", methods=["PUT"])
# @cross_origin()
# def editarEstadoSalon():
#     try:
#         a
#     except NoResultFound:
#         return "Salon not found", status.HTTP_401_UNAUTHORIZED

##Retorna todos los salones con solo el campo del estado
