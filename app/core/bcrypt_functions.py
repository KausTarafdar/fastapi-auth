from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    hashed_pw = bcrypt_context.hash(password)
    return hashed_pw

def verify_password(password: str, hash_password: str) -> bool:
    verify_pw = bcrypt_context.verify(password, hash_password)
    return verify_pw