
import hashlib
import os

def hash_password(password, salt=None):
    if not salt:
        salt = os.urandom(16)
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, hash_obj

if __name__ == "__main__":
    password = "mySecurePassword123"
    salt, hashed = hash_password(password)
    print(f"Password: {password}")
    print(f"Salt: {salt.hex()}")
    print(f"Hashed Password: {hashed.hex()}")
