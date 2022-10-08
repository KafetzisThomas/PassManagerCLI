#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os, sqlite3, Scripts.decrypt as decrypt, colorama
from colorama import Fore
colorama.init(autoreset=True)

# Printing out decrypted information from the database table inside the software 
# Encrypted data -> Decrypted data -> Printing out the data
def print_data():
    try:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM VAULT")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{Fore.LIGHTYELLOW_EX}--------------------------")
            for cell in row:
                print(decrypt.Decrypt(cell))
        
        print(f"{Fore.RED}\n*Your critical information are safe and protected!")
        connection.commit()
        connection.close()
    except sqlite3.OperationalError as err:
        print(f"{Fore.RED}{err}")
        connection.close()
        os.remove("data.db")