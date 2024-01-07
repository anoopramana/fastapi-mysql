#Connect this model to the database
from database import Base

#This file is what sqlalchemy (ORM) uses to create the tables in our database.
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

#Decide how many tables you need. 
#For this app we need two connected tables one for users and reflections
#In mysql the way we create a table is defining a class with the table attributes we want. 
#primary key and index are ways to ensure entries are unique
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True) 
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

class Reflections(Base):
    __tablename__ = 'reflections'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
