from flask_cors import CORS
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

cors = CORS()
migrate = Migrate()
redis = FlaskRedis()
api = Api()
db = SQLAlchemy()

def init_exts(app):
    cors.init_app(app=app)
    migrate.init_app(app=app,db=db)
    redis.init_app(app=app)
    api.init_app(app=app)
    db.init_app(app=app)
