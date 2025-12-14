import bcrypt
import jwt
from app.settings import APP_SETTINGS
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from ..core.handler.token import jwt_handler
from ..models.auth.auth import JWTPayload



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """
    Get the user ID from the given token.

    Args:
        token (str): The given token.

    Returns:
        str: The user ID.

    Raises:
        HTTPException: If the token is invalid or the user ID is not found.
    """
    try:
        payload = jwt_handler.decode_jwt_token(token)

        user_id = payload["data"].get("id", None)

        
 
    except (jwt.PyJWTError):
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

    
def encode_jwt_token(jwt_payload: JWTPayload) -> str:
    """
    Encode a JWT token with the given user email and ID.

    Args:
        email (str): The user email.
        id (str): The user ID.

    Returns:
        str: The encoded JWT token.
    """
    jwt_payload = jwt_payload.model_dump().copy()
    jwt_token = jwt.encode(jwt_payload, APP_SETTINGS.SECRET_KEY, algorithm=APP_SETTINGS.JWT_ALGORITHM)
    return jwt_token
   

def get_hashed_password(password: str) -> str:
    """
    Get the hashed password given the plain password.

    Args:
        password (str): The plain password.

    Returns:
        str: The hashed password.
    """

    salt = bcrypt.gensalt()
    bytes_password = password.encode('utf-8')
    binary_hash_password = bcrypt.hashpw(
        password=bytes_password,
        salt=salt
    )
    str_hashed_password = binary_hash_password.decode('utf-8')
    return str_hashed_password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify that the given plain password matches the given hashed password.

    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password=plain_password.encode('utf-8'), hashed_password=hashed_password.encode('utf-8'))