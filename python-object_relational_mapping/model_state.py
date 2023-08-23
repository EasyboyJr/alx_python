"""
A python file that contains the class definition of a State
and an instance Base = declarative_base():
"""
# import needed module
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create a variable to hold declarative_base
Base = declarative_base()


class State(Base):
    """
    A State class to represent a states table in MySQL
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
