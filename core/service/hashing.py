from passlib.context import CryptContext

pwd_hash = CryptContext(schemes=["bcrypt"], deprecated = "auto")

class Hash():
    def get_password_hashed(password):
        return pwd_hash.hash(password) 
    
    def verify_password(password: str, hashed_password: str):
        return pwd_hash.verify(password, hashed_password)
         