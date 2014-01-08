from sqlalchemy import Column, Integer, String, BLOB
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    salt = Column(String(64))
    password = Column(String(512))

    def __init__(self, name=None, email=None, password=None, salt=None):
        self.name = name
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self):
        return '<User %r>' % (self.name)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(BLOB)

    def __init__(self, user_id=None, content=None):
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return '<Entry %r>' % (self.id)

    def serialize(self):
       return {
           'id'      : self.id,
           'user_id' : self.user_id,
           'content' : self.content
       }