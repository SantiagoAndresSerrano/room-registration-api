from flask import Blueprint, request
from flask_api import status
from ..models.salon import Salon
from ..models.salon import salon_schema, salones_schema
from ..config.db import db
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

salones = Blueprint("salones",__name__)

##Returns all salones
@salones.route("/salon" , methods=["GET"])
@cross_origin()
def getAllSalones():
    try:
        all_salones = Salon.query.all()
        return salones_schema.dump(all_salones), status.HTTP_200_OK
    except NoResultFound:
        return "Salones not found", status.HTTP_401_UNAUTHORIZED

##Encontrar un salón
@salones.route("/salon/<string:id_salon>", methods=["GET"])
@cross_origin()
def encontrarSalon(id_salon):
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