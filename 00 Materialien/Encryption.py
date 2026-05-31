import base64
import hashlib
import os

# A quick and dirty implementation of a basic stream-chiffre.
# Pretty insecure from a modern standpoint, but works for demonstration purpose.

def enrypt(key: str, data: str) -> tuple[str, str]:
    """
    Encrypt data.

    :param key: Some key-string. The same key must be used to decrypt
    :param data: Data to encrypt
    :return: encrypted data, salt
    """
    data = data.encode()
    salt = base64.b85encode(os.urandom(16)).decode()
    key = hashlib.sha512((key + salt).encode()).digest() * (1 + len(data) // 16)
    data = bytes(map(lambda a: a[0] ^ a[1], zip(data, key)))
    return base64.b64encode(data).decode(), salt

def decrypt(key: str, data: str, salt: str) -> str:
    """
    Decrypt data.

    :param key:
    :param data: Encrypted data
    :param salt: Obtained from the encrypt-function
    :return: Decrypted data
    """
    data = base64.b64decode(data.encode())
    key = hashlib.sha512((key + salt).encode()).digest() * (1 + len(data) // 16)
    data = bytes(map(lambda a: a[0] ^ a[1], zip(data, key))).decode()
    return data


