from flask import Flask
from flask_restful import Api
from .routes import init_routes
from .database.db import init_db
from .bin.commands import passport
from flask_jwt_extended import JWTManager
from .config import LocalConfig, JWT_SECRET_KEY

app = Flask(__name__)
app.config.from_object(LocalConfig)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
api = Api(app)
app.register_blueprint(passport)
JWTManager(app)

init_db(app)
init_routes(api)
