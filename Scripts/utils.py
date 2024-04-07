#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import string, secrets
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


def generate_password(length, include_letters, include_digits, include_special_chars):
    """Return a random password string based on the provided options"""
    letters, digits, special_chars = (
        string.ascii_letters,
        string.digits,
        string.punctuation,
    )

    selected_chars = []
    if include_letters:
        selected_chars.append(letters)
    if include_digits:
        selected_chars.append(digits)
    if include_special_chars:
        selected_chars.append(special_chars)
    alphabet = "".join(selected_chars)

    password = ""
    for _ in range(length):
        password += "".join(secrets.choice(alphabet))
    return password
