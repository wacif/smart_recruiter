# utils/security_utils.py

from cryptography.fernet import Fernet

def generate_key():
    """Generates a key for encryption."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypts data with the specified key."""
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    """Decrypts encrypted data with the specified key."""
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()
