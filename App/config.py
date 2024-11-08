import datetime

# session
SECRET_KEY = 'happydays'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)

# DB
<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mm546896@localhost:3306/demo1'
=======
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/db'
>>>>>>> 03c102967b419fe8034f5b4727915c7fa85f78f1
SQLALCHEMY_TRACK_MODIFICATIONS = False

# redis
REDIS_URL = 'redis://localhost:6379/0'
