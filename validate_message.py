from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def fetch_public_key(user):
    with open(user+"key.pub","rb") as key_file:
        public_key=serialization.load_pem_private_key(
            key_file.read(),
            backend=default_backend())
        return public_key