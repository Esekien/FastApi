from typing import List
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import Userclass
from cryptography.fernet import Fernet

key = Fernet.generate_key()
keyRamdom = Fernet(key)

user = APIRouter()

@user.get('/', response_model=List[Userclass], tags=['users'])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post('/post_user', response_model=List[Userclass], tags=['users'])
def create_user(user: Userclass):
    new_user = {
        'name': user.name,
        'email': user.email,
        'password': keyRamdom.encrypt(user.password.encode("utf-8"))
    }
    result = conn.execute(users.insert().values(new_user))
    
    return 'user create with id: ' + str(result.lastrowid)

@user.get('/user/{id}',response_model=Userclass, tags=['users'])
def get_user(id: int):
    return  conn.execute(users.select().where(users.c.id == id)).first()

@user.delete('/user/delete/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/user/put/{id}', response_model=Userclass, tags=['users'])
def put_user(id: int, user: Userclass):
    conn.execute(users.update().values(
        name = user.name, 
        email = user.email, 
        password = keyRamdom.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))     
    return conn.execute(users.select().where(users.c.id == id)).first()