from cryptography.fernet import Fernet

def generateKey():
    key = Fernet.generate_key()
    with open("universal.key","wb") as key_file:
        key_file.write(key)