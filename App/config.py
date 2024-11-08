import datetime

# session
SECRET_KEY = 'happydays'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)

# DB
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mm546896@localhost:3306/demo1'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# redis
REDIS_URL = 'redis://localhost:6379/0'