#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3, sys, getpass, bcrypt
from Scripts.user import User
from prettytable import from_db_cursor
from cryptography.fernet import Fernet
from prettytable import PrettyTable

#key = Fernet.generate_key()

# ** this key is currently only for testing **
key = "-n9ISIWpULnLIGwatu-BDrf_Ob1xfhsKOZ_rbRn2KXU="


def create_connection():
    conn = sqlite3.connect("vault.db")
    cur = conn.cursor()
    return conn, cur

def create_credentials_table(cur):
        cur.execute("""CREATE TABLE credentials (
                    master_username text,
                    master_password text,
                    key
                    )""")

def create_items_table(cur):
        cur.execute("""CREATE TABLE IF NOT EXISTS items (
                    name text,
                    date_posted text,
                    website text,
                    username text,
                    password text,
                    notes text
                    )""")

def insert_data_to_credentials(conn, cur, user):
    with conn:
        cur.execute("INSERT INTO credentials VALUES (:master_username, :master_password, :key)", {'master_username': user.master_username, 'master_password': user.master_password, 'key': key})
    return key

def encrypt(message, key):
    return Fernet(key).encrypt(message)


def decrypt(token, key):
    return Fernet(key).decrypt(token)

def insert_data_to_items(conn, cur, item):
    f = Fernet(key)
    website = encrypt(item.website.encode(), key).decode('utf-8')
    username = encrypt(item.username.encode(), key).decode('utf-8')
    password = encrypt(item.password.encode(), key).decode('utf-8')
    notes = encrypt(item.notes.encode(), key).decode('utf-8')
    with conn:
        cur.execute("INSERT INTO items VALUES (:name, :date_posted, :website, :username, :password, :notes)", {'name': item.name, 'date_posted': item.date_posted, 'website': website, 'username': username, 'password': password, 'notes': notes})

def get_master_password_by_username(cur, master_username):
    cur.execute("SELECT * FROM credentials WHERE master_username=:master_username", {'master_username': master_username})
    return cur.fetchone()

#conn, cur = create_connection()
#print(get_master_password_by_username(cur, "thomas"))


def print_data(cur):
    cur.execute("SELECT name, username, password, website, notes, date_posted FROM items")
    mytable = PrettyTable(["Name", "Username", "Password", "Website", "Notes", "Date Posted"])

    for row in cur.fetchall():
        website = decrypt(row[3], key).decode()
        username = decrypt(row[1], key).decode()
        password = decrypt(row[2], key).decode()
        notes = decrypt(row[4], key).decode()
        mytable.add_row([row[0], username, password, website, notes, row[5]])

    print(mytable)


def update_data(conn, cur, colName, colValue, update_record):
    # Update data from table (vault)
    with conn:
        cur.execute(f"UPDATE items SET {colName} = ? WHERE name = ?", (colValue, update_record))


def delete_data(conn, cur, colName):
    # Delete data from table (vault)
    with conn:
        cur.execute('DELETE FROM items WHERE name = ?', (colName,))


def update_credentials_data(conn, cur, colValue, update_record):
    # Update data from table (vault)
    with conn:
        cur.execute(f"UPDATE credentials SET master_password = ? WHERE master_username = ?", (colValue, update_record))


def setup_login():
    # Ask the user for the existing master password
    # Get a hidden password input
    conn, cur = create_connection()
    create_credentials_table(cur)
    create_items_table(cur)
    master_username = input("\nMaster Username: ")
    master_password = getpass.getpass("\nMaster Password: ").encode('utf-8')
    if master_username != '' and master_password != '':
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(master_password, salt)
        user = User(master_username, hashed_password)
        insert_data_to_credentials(conn, cur, user)

def sign_in():
    _, cur = create_connection()
    master_username = input("\nMaster Username: ")
    master_password = getpass.getpass("\nMaster Password: ").encode('utf-8')
    stored_username = get_master_password_by_username(cur, master_username)
    print(stored_username)
    stored_password = get_master_password_by_username(cur, master_username)
    print(stored_password)
    try:
        if master_username == stored_username[0] and bcrypt.checkpw(master_password, stored_password[1]):
            print("ok")
        else:
            sys.exit()
    except TypeError:
        sys.exit()


def close_connection(conn):
    conn.close()
