#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from cryptography.fernet import Fernet


def generate_encryption_key():
    """Return a new encryption key"""
    key = Fernet.generate_key()
    return key


def encrypt(message, key):
    """Return an encrypted message (symmetric encryption)"""
    return Fernet(key).encrypt(message)


def decrypt(message, key):
    """Return a decrypted message (symmetric encryption)"""
    return Fernet(key).decrypt(message)
