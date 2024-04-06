#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3
from prettytable import PrettyTable
from Scripts.utils import generate_encryption_key, load_encryption_key, encrypt, decrypt


def create_connection():
    conn = sqlite3.connect("vault.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS credentials (
                master_username text,
                master_password text,
                encryption_key text
                )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS items (
                name text,
                date_posted text,
                website text,
                username text,
                password text,
                notes text
                )""")
    
    return conn, cur


def insert_data_to_credentials(conn, cur, user):
    encryption_key = generate_encryption_key()
    with conn:
        cur.execute("INSERT INTO credentials VALUES (:master_username, :master_password, :encryption_key)", {'master_username': user.master_username, 'master_password': user.master_password, 'encryption_key': encryption_key})


def insert_data_to_items(conn, cur, item):
    encryption_key = load_encryption_key(cur)
    website = encrypt(item.website.encode(), encryption_key).decode('utf-8')
    username = encrypt(item.username.encode(), encryption_key).decode('utf-8')
    password = encrypt(item.password.encode(), encryption_key).decode('utf-8')
    notes = encrypt(item.notes.encode(), encryption_key).decode('utf-8')
    with conn:
        cur.execute("INSERT INTO items VALUES (:name, :date_posted, :website, :username, :password, :notes)", {'name': item.name, 'date_posted': item.date_posted, 'website': website, 'username': username, 'password': password, 'notes': notes})


def get_current_master_password(cur, master_username):
    cur.execute("SELECT * FROM credentials WHERE master_username=:master_username", {'master_username': master_username})
    return cur.fetchone()


def print_items_data(cur):
    encryption_key = load_encryption_key(cur)
    cur.execute("SELECT name, username, password, website, notes, date_posted FROM items")
    mytable = PrettyTable(["Name", "Username", "Password", "Website", "Notes", "Date Posted"])

    for row in cur.fetchall():
        website = decrypt(row[3], encryption_key).decode()
        username = decrypt(row[1], encryption_key).decode()
        password = decrypt(row[2], encryption_key).decode()
        notes = decrypt(row[4], encryption_key).decode()
        mytable.add_row([row[0], username, password, website, notes, row[5]])

    print(mytable)


def update_credentials_data(conn, cur, old_master_username, master_username, master_password):
    # Update data from db (table: credentials)
    with conn:
        cur.execute("""UPDATE credentials SET master_username = :master_username, master_password = :master_password WHERE master_username = :old_master_username""",
                  {'old_master_username': old_master_username, 'master_username': master_username, 'master_password': master_password})


def update_items_data(conn, cur, colName, colValue, update_record):
    # Update data from db (table: items)
    encryption_key = load_encryption_key(cur)
    encrypted_colValue = encrypt(colValue.encode(), encryption_key).decode('utf-8')
    with conn:
        cur.execute(f"UPDATE items SET {colName} = ? WHERE name = ?", (encrypted_colValue, update_record))


def delete_data(conn, cur, colName):
    # Delete data from db (table: items)
    with conn:
        cur.execute('DELETE FROM items WHERE name = ?', (colName,))


def close_connection(conn):
    conn.close()
