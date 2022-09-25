from cryptography.fernet import Fernet

# Generating the universal key for authentication in process of data reading/encryption/decryption
def generateKey():
    key = Fernet.generate_key()
    with open("universal.key","wb") as key_file:
        key_file.write(key)