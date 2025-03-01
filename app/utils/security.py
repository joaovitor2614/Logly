import bcrypt
import jwt
from app.settings import APP_SETTINGS
from fastapi import Depends, HTTPException, status
from ..models.user import UserCreate, UserCrendentials
from fastapi.security import OAuth2PasswordBearer
from typing import Dict



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserCreate:
    try:
        payload = jwt.decode(token, APP_SETTINGS.SECRET_KEY, algorithms=[APP_SETTINGS.JWT_ALGORITHM])
        print('payload', payload)
        user_id = payload.get("id", None)

        
 
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user ID in token",
        )
    return user_id


def encode_jwt_token(user: Dict[str, str]) -> str:
    jwt_payload = {
        "name": user["name"],
        "email": user["email"],
        "id": str(user["_id"]),
    }
    jwt_token = jwt.encode(jwt_payload, APP_SETTINGS.SECRET_KEY, algorithm=APP_SETTINGS.JWT_ALGORITHM)
    return jwt_token
   

def get_hashed_password(password: str) -> str:

    salt = bcrypt.gensalt()
    bytes_password = password.encode('utf-8')
    binary_hash_password = bcrypt.hashpw(
        password=bytes_password,
        salt=salt
    )
    str_hashed_password = binary_hash_password.decode('utf-8')
    return str_hashed_password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password=plain_password.encode('utf-8'), hashed_password=hashed_password.encode('utf-8'))