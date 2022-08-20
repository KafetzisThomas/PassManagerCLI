import sqlite3
import decrypt
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def print_data():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM VAULT")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{Fore.LIGHTYELLOW_EX}--------------------------")
        for cell in row:
            print(decrypt.Decrypt(cell))   
    
    connection.commit()
    connection.close()