#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os, sqlite3, Scripts.decrypt as decrypt, colorama
from colorama import Fore as F
colorama.init(autoreset=True)

# Print decrypted information from the database table inside the software 
# Encrypt data -> Decrypt data -> Print data
def print_data():
    try:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Vault")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{F.LIGHTYELLOW_EX}------------------------------------------")
            for cell in row:
                print(decrypt.Decrypt(cell))
        
        connection.commit()
        connection.close()
    
    except sqlite3.OperationalError as err:
        print(f"{F.RED}{err}")
        connection.close()
        os.remove("data.db")