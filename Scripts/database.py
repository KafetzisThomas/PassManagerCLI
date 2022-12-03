#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from pysqlitecipher import sqlitewrapper
import time, sys, getpass, colorama
from colorama import Fore as F
colorama.init(autoreset=True)

# Set database settings
def set_database():
    global obj
    
    try:
        # Ask the user for the existing master password
        # Get a hidden password input
        pwd = getpass.getpass("\nMaster Password: ")
        if(pwd) != '':

            obj = sqlitewrapper.SqliteCipher(dataBasePath='data.db' , checkSameThread=True , password=pwd)
            print(f"\n> Logged in {F.GREEN}Successfully")

            colList = [
            ["name" , "TEXT"],
            ["username" , "TEXT"],
            ["password" , "TEXT"],
            ["website" , "TEXT"],
            ["note" , "TEXT"],
            ]

            # Create table
            obj.createTable('vault' , colList , makeSecure=True , commit=True)
        else:
            print(f"{F.RED}You did not fill the field.")
            set_database()
    except ValueError:
        pass
    except RuntimeError:
        print(f"{F.RED}Incorrect password.")
        set_database()
    except KeyboardInterrupt:
        print(f"\nExiting in {F.RED}5{F.RESET} seconds...")
        time.sleep(5)
        sys.exit()

def insert_data(name,username,password,website,note):
    # Combination of input data
    insertList = (name, username, password, website, note)

    # Insert data into table (vault)
    obj.insertIntoTable('vault' , insertList , commit = True)

def print_data():
    print(f"\n{F.LIGHTYELLOW_EX}================ My Vault ================")
    # Print the data from the database table as decrypted
    insert_data = (obj.getDataFromTable('vault' , raiseConversionError = True , omitID = False))
    for i in insert_data[1:]:
        for x in i:
            print(f"{F.LIGHTYELLOW_EX}------------------------------------------")
            for j in x:
                print(j)
    time.sleep(1)

def delete_data():
    # Ask user for which record to be deleted
    delete_id = int(input("\n\nWhich specific record (ID) do you want to delete from the vault?\n> "))

    # Delete data from a table
    obj.deleteDataInTable('vault' , delete_id , commit = True , raiseError = True , updateId = True)

def change_master_password():
    # Ask for a new master password
    # Get a hidden password input
    new_password = input("Master Password: ")
    for i in obj.changePassword(new_password):
        print("Password changed.")
