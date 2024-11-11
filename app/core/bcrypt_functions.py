from bcrypt import gensalt, hashpw, checkpw

salt = gensalt()

def hash_password(password: str) -> str:
    pw_bytes = password.encode('utf-8')
    hashed_pw = hashpw(pw_bytes, salt)
    return hashed_pw

def verify_password(password: str, hash_password: str) -> bool:
    pw_bytes = password.encode('utf-8')
    verify_pw = checkpw(pw_bytes, hash_password)
    return verify_pw