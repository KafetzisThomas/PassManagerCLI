#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import string, secrets
from cryptography.fernet import Fernet


def encrypt(message, key):
    return Fernet(key).encrypt(message)


def decrypt(token, key):
    return Fernet(key).decrypt(token)


def generate_password():
  '''Generate a secure password'''
  letters, digits, special_chars = string.ascii_letters, string.digits, string.punctuation
  alphabet = (letters + digits + special_chars)  # Define the alphabet

  pwd_length = int(input("\nEnter password length: "))  # Set password length

  password = ''
  for _ in range(pwd_length):
    password += ''.join(secrets.choice(alphabet))  # Generate a password string
  return password
