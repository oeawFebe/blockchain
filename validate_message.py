from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def fetch_public_key(user):
    with open(user.decode("ascii")+"key.pub","rb") as key_file:
        public_key=serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend())
        return public_key
# Message coming from user
message=b"Nelson likes cat"
#Signature coming from user, this is very specific to public key
signature=b"\xc4\xf6v\xa9\xdc\x8d\xc9\xa4pY\xd4\x00\x92J\xe8\xf3y\x98\x9e\x83\xe3KG\xd6?d\xb0\xc4\xa4D\x04\xa9\xecX\x95\xca\xaa\xd3\xa7\xcf)\x99rTOz\xe6~\x8e\x02\x85eB'\xf0p_\x08w\x1f\xce\xd7\xc8\x0co\xb5\xcaZ\xfe8\x05;\x83rp\x9f\x8a]E\xcc4\x89Vwz\x86\xf6\x93~\xa8p\xa7\xe7c5DH\x04Z.\x80\x017\xe7\x18\x15m\x85t\x84\x83\xc5\xa9\x0b\x92\x9b\x0f\xa5L\xc0\xa8)\x03f\n\x8dV\xbd"

user=message.split()[0].lower()
# fetch public key from Nelson
public_key=fetch_public_key(user)
public_key.verify(
    signature,
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256())
