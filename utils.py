from cryptography.fernet import Fernet
import os

KEY_PATH = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_PATH):
        generate_key()
    return open(KEY_PATH, "rb").read()
