from flask import Blueprint, request
from flask_api import status
from ..models.horario import Horario
from ..models.horario import horario_schema, horarios_schema
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

horarios = Blueprint("horarios",__name__)

##Retorna todos los horarios
@horarios.route("/horario" , methods=["GET"])
@cross_origin()
def getAllHorarios():
    try:
        all_horarios = Horario.query.all()
        return horarios_schema.dump(all_horarios), status.HTTP_200_OK
    except NoResultFound:
        return "Horarios not found", status.HTTP_401_UNAUTHORIZED

##Encontrar un horario
@horarios.route("/horario/<string:id_horario>", methods=["GET"])
@cross_origin()
def encontrarHorario(id_horario):
    try:
        horarioFound = Horario.query.filter(Horario.id_horario == id_horario).one()
    except NoResultFound:
        return "Horario not found", status.HTTP_401_UNAUTHORIZED
    return horario_schema.dump(horarioFound), status.HTTP_200_OK
