from flask import Blueprint, request
from flask_api import status
from ..config.db import db
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

from ..models.materia import Materia, materia_schema, materias_schema
from ..models.grupo_materia import GrupoMateria, grupo_materia_schema, grupos_materia_schema

materias = Blueprint("materias",__name__)

#Retorna all materias
@materias.route("/materia" , methods=["GET"])
@cross_origin()
def getAllMateria():
    try:
        all_materia = Materia.query.all()
        return materias_schema.dump(all_materia), status.HTTP_200_OK
    except NoResultFound:
        return "Materias not found", status.HTTP_401_UNAUTHORIZED
    
#Retorna todos los grupos materia existentes(115304-A)
@materias.route("/materia/grupos", methods=["GET"])
@cross_origin()
def getGrupoMateria():
    try:
        all_grupos = GrupoMateria.query.all()
        return grupos_materia_schema.dump(all_grupos), status.HTTP_200_OK
    except NoResultFound:
        return "Grupos de materias not found", status.HTTP_401_UNAUTHORIZED