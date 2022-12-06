from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flasgger import Swagger, LazyString, LazyJSONEncoder
import os
from dotenv import load_dotenv


from .models.grupo_materia import GrupoMateria, grupos_materia_schema

from .routes.materia import materias
from .routes.inventario import inventario
from .routes.bloque import bloques
from .routes.salon import salones
from .routes.horario import horarios


def create_app(test_config=None):
    swagger_template = {
        "info": {
            'title': 'Api Python Test',
            'version': '0.1',
            'description': 'This document contains the list of API services '
                           'with Python.',
        },
        "host": "web-production-a9da.up.railway.app/",
        #   "host":"room-registration-microservice.herokuapp.com",
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": 'JWT Authorization header using the Bearer scheme. '
                               'Example: "Authorization: Bearer {token}"'
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    swagger = Swagger(app, template=swagger_template)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    load_dotenv()

    app.config['JSON_AS_ASCII'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://uz7o2tfmyylgx2xam70s:IF42pKqz6mS1Qgl4VCFx@b7ajzb3arliywy9f1q9k-postgresql.services.clever-cloud.com:5432/b7ajzb3arliywy9f1q9k"
    app.config.from_mapping(
       # SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE='postgresql://uz7o2tfmyylgx2xam70s:IF42pKqz6mS1Qgl4VCFx@b7ajzb3arliywy9f1q9k-postgresql.services.clever-cloud.com:5432/b7ajzb3arliywy9f1q9k'
    )
    
    #Deshabilitar el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False 
    
    ##Registro de Blueprints
    app.register_blueprint(bloques)
    app.register_blueprint(salones)
    app.register_blueprint(inventario)
    app.register_blueprint(materias)
    app.register_blueprint(horarios)
    
    db.init_app(app)
    ma.init_app(app)
    

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    return app

