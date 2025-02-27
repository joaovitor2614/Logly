import bcrypt


def get_hashed_password(password: str) -> str:

    salt = bcrypt.gensalt()
    bytes_password = password.encode('utf-8')
    binary_hash_password = bcrypt.hashpw(
        password=bytes_password,
        salt=salt
    )
    str_hashed_password = binary_hash_password.decode('utf-8')
    return str_hashed_password