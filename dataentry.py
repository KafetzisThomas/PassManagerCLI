import sqlite3, encrypt

# Importing encrypted data into the database
def enter_data(name,username,password,website):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    table = """INSERT INTO VAULT(name,username,password,website)
            VALUES (?,?,?,?);"""
    
    name = encrypt.Encrypt(name)
    username = encrypt.Encrypt(username)
    password = encrypt.Encrypt(password)
    website = encrypt.Encrypt(website)

    combination = (name,username,password,website)
    cursor.execute(table,combination)
    connection.commit()
    connection.close()