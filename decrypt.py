from cryptography.fernet import Fernet

# Loading the universal key for authentication in process of data reading/decryption
def loadKey():
    key = open("universal.key","rb").read()
    return key

# Decrypting the data of the database table (VAULT)
def Decrypt(encrypt_key):
    key = loadKey()
    fernet  = Fernet(key)
    decryptKey = fernet.decrypt(encrypt_key)
    return decryptKey.decode()