from cryptography.fernet import Fernet

def encrypt_file(file_bytes, key):
    f = Fernet(key)
    return f.encrypt(file_bytes)

def decrypt_file(file_bytes, key):
    f = Fernet(key)
    return f.decrypt(file_bytes)