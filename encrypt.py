from cryptography.fernet import Fernet

def loadKey():
    key = open("universal.key","rb").read()
    return key

def Encrypt(secret_key):
    key = loadKey()
    encodeKey = secret_key.encode()
    fernet  = Fernet(key)
    return fernet.encrypt(encodeKey)