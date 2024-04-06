#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import string, secrets
from cryptography.fernet import Fernet


def generate_encryption_key():
    key = Fernet.generate_key()
    return key


def load_encryption_key(cur):
    cur.execute("SELECT encryption_key FROM credentials")
    return cur.fetchone()[0]


def encrypt(message, key):
    return Fernet(key).encrypt(message)


def decrypt(token, key):
    return Fernet(key).decrypt(token)


def generate_password(pwd_length, password = ''):
    """Return a generated password string"""
    letters, digits, special_chars = string.ascii_letters, string.digits, string.punctuation
    alphabet = letters + digits + special_chars

    for _ in range(pwd_length):
        password += ''.join(secrets.choice(alphabet))
    return password
