from flask import Blueprint, request
from flask_api import status
from app.models.salon import Salon, salones_schema, SalonSchema
from ..models.bloque import Bloque
from ..models.bloque import bloque_schema, bloques_schema
from ..config.db import db
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound
from flask_cors import cross_origin

bloques = Blueprint("bloques",__name__)

#Retorna all bloques
@bloques.route("/roomregister/bloque" , methods=["GET"])
@cross_origin()
def getAllBloques():
    """Returning list all Bloques
    ---
    tags:
      - Bloque
    definitions:
      Bloque:
        type: object
        properties:
          id_edificio:
            type: integer
          nombre:
            type: string
          piso:
            type: integer 
    responses:
      200:
        description: A list of Bloques
        schema:
          $ref: '#/definitions/Bloque'
    """
    try:
        all_bloque = Bloque.query.all()
        return bloques_schema.dump(all_bloque), status.HTTP_200_OK
    except NoResultFound:
        return "Bloques not found", status.HTTP_401_UNAUTHORIZED
      
      #Retorna all bloques
@bloques.route("/roomregister/bloque/<int:id_edificio>" , methods=["GET"])
@cross_origin()
def getAllSalonBloque(id_edificio):
    """Returning list all room class by bloque
    ---
    tags:
      - Bloque
    parameters:
      - name: id_edificio
        in: path
        type: integer
        required: true
        description: Identifier bloque, example (1)
    definitions:
      Salon:
        type: object
        properties:
          id_salon:
            type: string
    responses:
      200:
        description: A list of rooms
        schema:
          $ref: '#/definitions/Bloque'
    """
    try:
        all_salon = Salon.query.filter(Salon.bloque == id_edificio)
        salones1_schema = SalonSchema(many=True, only=('id_salon',))
        return salones1_schema.dump(all_salon), status.HTTP_200_OK
    except NoResultFound:
        return "Salones not found", status.HTTP_401_UNAUTHORIZED
