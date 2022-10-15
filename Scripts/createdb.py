#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3

# Creating the database (data.db)
def create_database():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    table = """CREATE TABLE VAULT(
            name VARCHAR(10000) PRIMARY KEY,
            username VARCHAR(10),
            password VARCHAR(5),
            website VARCHAR(10),
            note VARCHAR(5));"""
    
    cursor.execute(table)
    connection.commit()
    connection.close()