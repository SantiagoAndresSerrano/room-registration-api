from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import os
from dotenv import load_dotenv

from .models.grupo_materia import GrupoMateria, grupos_materia_schema

from .routes.materia import materias
from .routes.inventario import inventario
from .routes.bloque import bloques
from .routes.salon import salones
from .routes.horario import horarios


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    load_dotenv()

    app.config['JSON_AS_ASCII'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://uz7o2tfmyylgx2xam70s:IF42pKqz6mS1Qgl4VCFx@b7ajzb3arliywy9f1q9k-postgresql.services.clever-cloud.com:5432/b7ajzb3arliywy9f1q9k"
    app.config.from_mapping(
       # SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE='postgresql://uz7o2tfmyylgx2xam70s:IF42pKqz6mS1Qgl4VCFx@b7ajzb3arliywy9f1q9k-postgresql.services.clever-cloud.com:5432/b7ajzb3arliywy9f1q9k'
    )
    
    ##Blueprints
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
    
# #getAll
#     @app.route("/api/detallehorario/")
#     def getDetalleHorario():
#         all = DetalleHorario.query.all()
#         return dets_horario_schema.jsonify(all)


    return app

