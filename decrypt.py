from cryptography.fernet import Fernet

def loadKey():
    key = open("universal.key","rb").read()
    return key

def Decrypt(encrypt_key):
    key = loadKey()
    fernet  = Fernet(key)
    decryptKey = fernet.decrypt(encrypt_key)
    return decryptKey.decode()