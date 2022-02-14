""" Autenticação para usar o FastAPI """

from schemas import User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Autenticação
usuario = {
    "igor": {
        "username": "igor",
        "full_name": "Igor Esposito",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    },
}

def fake_hash_password(password: str):
    """ Separa o hash da senha """
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserInDB(User):
    """ Usuário ativo """
    hashed_password: str

def get_user(db_usuario, username: str):
    """ Retorna o usuário """
    if username in db_usuario:
        user_dict = db_usuario[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    """ Decodifica o token """
    user = get_user(usuario, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """ Retorna o usuário ativo """
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """ Validação de usuário ativo """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
