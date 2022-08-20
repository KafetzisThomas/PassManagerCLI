import sqlite3
import decrypt

def print_data():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM VAULT")
    rows = cursor.fetchall()
    for row in rows:
        print("--------------------------\n")
        for cell in row:
            print(decrypt.Decrypt(cell))   
    
    print("\n* Your critical information are safe and protected!")
    connection.commit()
    connection.close()