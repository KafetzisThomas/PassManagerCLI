#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3, Scripts.encrypt as encrypt

# Import encrypted data into the database
def enter_data(name,username,password,website,note):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    table = """INSERT INTO Vault(name,username,password,website,note)
            VALUES (?,?,?,?,?);"""
    
    name = encrypt.Encrypt(name)
    username = encrypt.Encrypt(username)
    password = encrypt.Encrypt(password)
    website = encrypt.Encrypt(website)
    note = encrypt.Encrypt(note)

    combination = (name,username,password,website,note)
    cursor.execute(table,combination)
    connection.commit()
    connection.close()