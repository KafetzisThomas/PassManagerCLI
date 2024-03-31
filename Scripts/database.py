#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sqlite3, sys, getpass, bcrypt
from Scripts.user import User


def create_connection():
    conn = sqlite3.connect("vault.db")
    cur = conn.cursor()
    return conn, cur

def create_credentials_table(cur):
        cur.execute("""CREATE TABLE credentials (
                    master_username text,
                    master_password text
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
        cur.execute("INSERT INTO credentials VALUES (:master_username, :master_password)", {'master_username': user.master_username, 'master_password': user.master_password})


def insert_data_to_items(conn, cur, item):
    with conn:
        cur.execute("INSERT INTO items VALUES (:name, :date_posted, :website, :username, :password, :notes)", {'name': item.name, 'date_posted': item.date_posted, 'website': item.website, 'username': item.username, 'password': item.password, 'notes': item.notes})

def get_master_password_by_username(cur, master_username):
    cur.execute("SELECT * FROM credentials WHERE master_username=:master_username", {'master_username': master_username})
    return cur.fetchone()

#conn, cur = create_connection()
#print(get_master_password_by_username(cur, "thomas"))


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
