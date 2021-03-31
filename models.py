from sqlalchemy import Column, Integer, String
from database import Base
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(128))
    email = Column(String(120), unique=True)
    date = Column(String(15), default=datetime.now)
    points = Column(Integer,default=0)
    permit = Column(Integer,default=0)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)