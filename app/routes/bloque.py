from flask import Blueprint, request
from flask_api import status
from ..models.bloque import Bloque
from ..models.bloque import bloque_schema, bloques_schema
from ..config.db import db
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

bloques = Blueprint("bloques",__name__)

#Retorna all bloques
@bloques.route("/bloque" , methods=["GET"])
@cross_origin()
def getAllBloques():
    try:
        all_bloque = Bloque.query.all()
        return bloques_schema.dump(all_bloque), status.HTTP_200_OK
    except NoResultFound:
        return "Bloques not found", status.HTTP_401_UNAUTHORIZED