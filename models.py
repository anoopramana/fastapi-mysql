#This file is what sqlalchemy (ORM) uses to create the tables in our database.

from sqlalchemy import Boolean, Column, Integer, String

#Connect this model to the database
from database import Base

#Decide how many tables you need. 
#For this app we need two connected tables one for users and reflections
#In mysql the way we create a table is defining a class with the table attributes we want. 
#primary key and index are ways to ensure entries are unique
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String(50), unique=True) 


class Post(Base):
    __tablename__ = 'reflections'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(500))
    user_id = Column(Integer)


