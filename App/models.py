
from sqlalchemy import Integer,String
from sqlalchemy.orm import MappedColumn

from .extentions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    age = db.Column(db.Integer,default=15)
    gender = db.Column(db.Boolean,default=1)

class User2(db.Model):
    __tablename__ = 'user2'
    id= MappedColumn(Integer,primary_key=True,autoincrement=True)
    name= MappedColumn(String(20),unique=True,nullable=False)
    like= MappedColumn(String(20))
    hobby= MappedColumn(String(20))
    hobbyxxx = MappedColumn(String(20))
    test = MappedColumn(String(20),unique=True,nullable=False)
