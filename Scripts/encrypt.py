#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from cryptography.fernet import Fernet

# Loading the universal key for authentication in process of data reading/encryption
def loadKey():
    key = open("universal.key","rb").read()
    return key

# Encrypting the data of the database table (VAULT)
def Encrypt(secret_key):
    key = loadKey()
    encodeKey = secret_key.encode()
    fernet  = Fernet(key)
    return fernet.encrypt(encodeKey)