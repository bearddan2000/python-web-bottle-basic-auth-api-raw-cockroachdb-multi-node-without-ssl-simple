from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DbModel(Base):
    __tablename__ = 'dog'

    id = Column(Integer, primary_key=True)
    breed = Column(String())
    color = Column(String())

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def __str__(self):
        return f"<Dog {self.id}, {self.breed}, {self.color}>"
