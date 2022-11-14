from flask import Blueprint, request
from flask_api import status

from app.models.detalle_horario import det_horario_schema
from app.models.salon import Salon
from app.models.grupo_materia import GrupoMateria
from sqlalchemy import and_
from ..models.detalle_horario import DetalleHorario, det_horario_schema, dets_horario_schema
from ..models.horario import Horario
from ..models.horario import horario_schema, horarios_schema
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

horarios = Blueprint("horarios",__name__)

##Retorna todos los horarios
@horarios.route("/roomregister/horario" , methods=["GET"])
@cross_origin()
def getAllHorarios():
    """Returning list all horario
    ---
    tags:
      - Horario
    definitions:
      Horario:
        type: object
        properties:
          id_horario:
            type: integer
          dia:
            type: string
          hora_inicio:
            type: string
            format: date-time
          hora_final:
            type: string
            format: date-time
    responses:
      200:
        description: A list of Horario
        schema:
          $ref: '#/definitions/Horario'
    """
    try:
        all_horarios = Horario.query.all()
        return horarios_schema.dump(all_horarios), status.HTTP_200_OK
    except NoResultFound:
        return "Horarios not found", status.HTTP_401_UNAUTHORIZED

##Encontrar un horario
@horarios.route("/roomregister/horario/<string:id_horario>", methods=["GET"])
@cross_origin()
def encontrarHorario(id_horario):
    """Returning A Horario
    ---
    tags:
      - Horario
    parameters:
      - name: id_horario
        in: path
        type: integer
        required: true
        description: Identifier horario
    definitions:
      Horario:
        type: object
        properties:
          id_horario:
            type: integer
          dia:
            type: string
          hora_inicio:
            type: string
            format: date-time
          hora_final:
            type: string
            format: date-time
    responses:
      200:
        description: A Horario
        schema:
          $ref: '#/definitions/Horario'
    """
    try:
        horarioFound = Horario.query.filter(Horario.id_horario == id_horario).one()
    except NoResultFound:
        return "Horario not found", status.HTTP_401_UNAUTHORIZED
    return horario_schema.dump(horarioFound), status.HTTP_200_OK

##Retorna todos los horarios
@horarios.route("/roomregister/horario/detalle" , methods=["GET"])
@cross_origin()
def getAllDetailsHorarios():
    """Returning list details all horario
    ---
    tags:
      - Horario
    definitions:
      Horario:
        type: object
        properties:
          id_horario:
            type: integer
          dia:
            type: string
          hora_inicio:
            type: string
            format: date-time
          hora_final:
            type: string
            format: date-time
    responses:
      200:
        description: A list of Horario
        schema:
          $ref: '#/definitions/Horario'
    """
    try:
        all_horarios = DetalleHorario.query.all()
        return dets_horario_schema.dump(all_horarios), status.HTTP_200_OK
    except NoResultFound:
        return "Horarios not found", status.HTTP_401_UNAUTHORIZED

##Retorna todos los horarios
@horarios.route("/roomregister/horariosalon/<string:id_salon>" , methods=["GET"])
@cross_origin()
def getAllDetailsHorariosBySalon(id_salon):
    """Returning list details all horario by Salon
    ---
    tags:
      - Horario
    parameters:
      - name: id_salon
        in: path
        type: string
        required: true
        description: Identifier Salón
    definitions:
      Horario:
        type: object
        properties:
          id_horario:
            type: integer
          dia:
            type: string
          hora_inicio:
            type: string
            format: date-time
          hora_final:
            type: string
            format: date-time
    responses:
      200:
        description: A list of Horario
        schema:
          $ref: '#/definitions/Horario'
    """
    try:
        all_horarios = Horario.query.join(DetalleHorario).filter(and_(Salon.id_salon==id_salon, GrupoMateria.id_grup_mat==Salon.grupo_materia, DetalleHorario.grupo_materia == GrupoMateria.id_grup_mat, DetalleHorario.horario == Horario.id_horario))
        return horarios_schema.dump(all_horarios), status.HTTP_200_OK
    except NoResultFound:
        return "Horarios not found", status.HTTP_401_UNAUTHORIZED