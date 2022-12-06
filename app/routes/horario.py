from flask import Blueprint, request
from flask_api import status

from app.models.detalle_horario import det_horario_schema, DetalleHorarioSchema
from app.models.salon import Salon
from app.models.grupo_materia import GrupoMateria
from sqlalchemy import and_
from ..models.detalle_horario import DetalleHorario, det_horario_schema, dets_horario_schema
from ..models.horario import Horario
from ..models.horario import horario_schema, horarios_schema
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin
from datetime import datetime 

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
      

@horarios.route("/roomregister/horario/<string:id_salon>/<int:dia>", methods=["GET"])
@cross_origin()
def consultarHorarioSalon(id_salon, dia):
    """Retorna el horario de un salón determinado día
      ---
      tags:
        - Horario
      parameters:
        - name: id_salon
          in: path
          type: string
          required: true
          description: Identifier salon, example (SA401)
        - name: dia
          in: path
          type: integer
          required: true
          description: Identifier dia, example (0-6)
      responses:
        200:
          description: list horario
          schema:
            $ref: '#/definitions/Horario'
      """
    try:
        detalleHorarioFound = Horario.query.join(DetalleHorario).join(GrupoMateria).join(Salon).filter(and_(Salon.id_salon== id_salon, GrupoMateria.id_grup_mat==Salon.grupo_materia, DetalleHorario.grupo_materia == GrupoMateria.id_grup_mat, Horario.id_horario == DetalleHorario.id_det_hor, Horario.dia == dia))
    except NoResultFound:
        return "no detail with this schedule can be found", status.HTTP_401_UNAUTHORIZED
    return horarios_schema.dump(detalleHorarioFound), status.HTTP_200_OK

@horarios.route("/roomregister/horario/fecha/<string:id_salon>/<string:fecha>", methods=["GET"])
@cross_origin()
def consultarHorarioSalonFecha(id_salon, fecha):
    """Retorna el horario de un salón determinado día
      ---
      tags:
        - Horario
      parameters:
        - name: id_salon
          in: path
          type: string
          required: true
          description: Identifier salon, example (SA401)
        - name: fecha
          in: path
          type: string
          format: date-time
          required: true
          description: Identifier dia, example (2022-08-15 10:10:00)
      responses:
        200:
          description: list horario
          schema:
            $ref: '#/definitions/Horario'
      """
    try:
        dia = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S").weekday()
        print(dia)
        detalleHorarioFound = Horario.query.join(DetalleHorario).join(GrupoMateria).join(Salon).filter(and_(Salon.id_salon== id_salon, GrupoMateria.id_grup_mat==Salon.grupo_materia, DetalleHorario.grupo_materia == GrupoMateria.id_grup_mat, Horario.id_horario == DetalleHorario.id_det_hor, Horario.dia == dia))
    except NoResultFound:
        return "no detail with this schedule can be found", status.HTTP_401_UNAUTHORIZED
    return horarios_schema.dump(detalleHorarioFound), status.HTTP_200_OK
