#all connection strings for our app to connect to mysql

#Create an engine that enables database to communicate to our app 
from sqlalchemy import create_engine
#
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#link to databse 
URL_DATABASE = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/ReflectionAppDatabase'

#Sometimes its better to hide the username and passwords in apps:
# import os
# user = os.environ["MYSQL_USER"]
# password = os.environ["MYSQL_PASSWORD"]
# uri = f"mysql://{user}:{password}@example.com/testdb"

#create an engine variable with link to database
engine = create_engine(URL_DATABASE)

#Create a configured session factory class. Sessionmaker acts as a factory for Session. Engine acts as a factory for Connection. 
#Autocommit = 
#Autoflush = 
#Bind = all SQL operations performed by this session will execute via this connectable.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


