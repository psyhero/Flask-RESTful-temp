from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_redis import FlaskRedis
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE':'simple'})
api = Api()
redis = FlaskRedis()

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    cache.init_app(app=app)
    redis.init_app(app=app)
    api.init_app(app=app)
