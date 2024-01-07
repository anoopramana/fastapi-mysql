#Main file for fastapi application
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext

#As with every Fastapi app you need to initiate the app 
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

#Create pydantic models
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

#create our dependency for our database in our app
    #create a method of get_db using our sessionlocal connection. 
    #we'll try getting our db then close the db connection as we don't want to keep it open for too long.
def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()

#Now we need a way to route the get_db function to get a database session. 
db_dependency = Annotated[Session, Depends(get_db)]


#Create first fastapi endpoit to create and save a user 

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()

async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()
    
    
@app.get("/")
def read_root():
    return {"Hello you massive legend. You've just successfully connected a fast api app with a mysql database to a web browser"}