from flask import Blueprint, request
from flask_api import status
import flask_sqlalchemy
import sqlalchemy
from app.models.horario import Horario
from app.models.grupo_materia import GrupoMateria
from app.models.salon import SalonSchema
from ..models.salon import salon_schema, salones_schema, Salon
from ..models.detalle_horario import  DetalleHorario
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin
from sqlalchemy import and_

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
  
  ##Consultar estado de un salón
@salones.route("/roomregister/salon/estado/<string:id_salon>/<string:fechaInicio>/<string:fechaFin>", methods=["GET"])
@cross_origin()
def consultarSalon(id_salon, fechaInicio, fechaFin):
    """Retorna el estado de un salón en un horario determinado
      ---
      tags:
        - Salon
      parameters:
        - name: id_salon
          in: path
          type: string
          required: true
          description: Identifier salon, example (SA401)
        - name: fecha inicial
          in: path
          type: string
          format: date-time
          required: true
          description: Identifier fecha inicial, example (2022-08-15 10:10:00)
        - name: fecha final
          in: path
          type: string
          format: date-time
          required: true
          description: Identifier fecha final, example (2022-08-15 12:10:00)
      definitions:
        Salon:
          type: object
          properties:
            id_salon:
              type: string
            estado:
              type: integer
      responses:
        200:
          description: condition of a room class
          schema:
            $ref: '#/definitions/Salon'
      """
    try:
        salonFound = Salon.query.join(GrupoMateria).join(DetalleHorario).filter(and_(Salon.id_salon== id_salon, GrupoMateria.id_grup_mat==Salon.grupo_materia, DetalleHorario.grupo_materia == GrupoMateria.id_grup_mat,fechaInicio == Horario.hora_inicio, fechaFin == Horario.hora_final)).one()
        salon1_schema = SalonSchema(only=('id_salon','estado'))
    except NoResultFound:
        return "Salon not found", status.HTTP_401_UNAUTHORIZED
    return salon1_schema.dump(salonFound), status.HTTP_200_OK

##Editar el estado de un determinado salón 
# @salones.route("/salon/<string:salon>", methods=["PUT"])
# @cross_origin()
# def editarEstadoSalon():
#     try:
#         a
#     except NoResultFound:
#         return "Salon not found", status.HTTP_401_UNAUTHORIZED

##Retorna todos los salones con solo el campo del estado
