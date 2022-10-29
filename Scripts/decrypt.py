#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from cryptography.fernet import Fernet

# Load the universal key for authentication in process of data reading/decryption
def loadKey():
    key = open("universal.key","rb").read()
    return key

# Decrypt the data of the database table (Vault)
def Decrypt(encrypt_key):
    key = loadKey()
    fernet  = Fernet(key)
    decryptKey = fernet.decrypt(encrypt_key)
    return decryptKey.decode()