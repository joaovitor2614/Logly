import bcrypt
import jwt
from dotenv import load_dotenv
import os
from typing import Dict
config = load_dotenv()

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")



def encode_jwt_token(user: Dict[str, str]) -> str:
    jwt_payload = {
        "name": user["name"],
        "email": user["email"],
        "id": str(user["_id"]),
    }
    jwt_token = jwt.encode(jwt_payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
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