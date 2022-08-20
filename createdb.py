import sqlite3

def create_database():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    table = """CREATE TABLE VAULT(
            username VARCHAR(10000) PRIMARY KEY,
            password VARCHAR(5),
            email VARCHAR(5),
            url VARCHAR(10));"""
    
    cursor.execute(table)
    connection.commit()
    connection.close()