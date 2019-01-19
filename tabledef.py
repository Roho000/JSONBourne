from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()

########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    balance = Column(Integer)

#----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password
        self.balance = 0

# create tables
Base.metadata.create_all(engine)
