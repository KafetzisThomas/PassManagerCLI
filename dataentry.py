import sqlite3
import encrypt 

def enter_data(username,password,email,url):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    table = """INSERT INTO VAULT(username,password,email,url)
            VALUES (?,?,?,?);"""
    
    username = encrypt.Encrypt(username)
    password = encrypt.Encrypt(password)
    email = encrypt.Encrypt(email)
    url = encrypt.Encrypt(url)

    combination = (username,password,email,url)
    cursor.execute(table,combination)
    connection.commit()
    connection.close()