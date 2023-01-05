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

            obj = sqlitewrapper.SqliteCipher(dataBasePath='vault.db' , checkSameThread=True , password=pwd)
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
    print(f"\n{F.LIGHTYELLOW_EX}============= My Vault =============")
    # Print the data from the database table as decrypted
    insert_data = (obj.getDataFromTable('vault' , raiseConversionError = True , omitID = False))
    for i in insert_data[1:]:
        for x in i:
            print(f"{F.LIGHTYELLOW_EX}------------------------------------") 
            print(f"ID:       \t{F.CYAN}{x[0]}")
            print(f"Name:     \t{F.GREEN}{x[1]}")
            print(f"Username: \t{F.GREEN}{x[2]}")
            print(f"Password: \t{F.GREEN}{x[3]}")
            print(f"Website:  \t{F.GREEN}{x[4]}")
            print(f"\nNote:     \t{F.GREEN}{x[5]}")

    time.sleep(1)

def delete_data():
    # Ask user for which record (ID) of the row want data to be deleted
    delete_id = int(input("\n\nWhich specific record (ID) do you want to delete from the vault?\n> "))

    # Delete data from table (vault)
    obj.deleteDataInTable('vault' , delete_id , commit = True , raiseError = True , updateId = True)

def update_data():
    # Ask user for which record (ID) of the row want data to be updated
    update_id = int(input(f"\n\nWhich specific {F.LIGHTRED_EX}record (ID){F.RESET}"
                            f" do you want to {F.LIGHTBLUE_EX}update{F.RESET} from the vault?\n> "))
    
    # Ask user for name of the column to change value in row
    colName = input(f"\nWhich specific {F.LIGHTCYAN_EX}column name{F.RESET}"
                        f" do you want to update from the {F.LIGHTMAGENTA_EX}vault{F.RESET}?"
                            "\n\t(name,username,password,website,note)\n> ").lower()
    
    # Ask user for new value to be inserted into colName
    colValue = input(f"\nWrite {F.LIGHTBLUE_EX}new{F.RESET} item:\n> ").strip()

    # Update data from table (vault)
    obj.updateInTable('vault' , update_id , colName , colValue , commit = True , raiseError = True)

def change_master_password():
    # Ask for a new master password
    # Get a hidden password input
    new_password = getpass.getpass("\nMaster Password: ")
    for i in obj.changePassword(new_password):
        print("Password changed.")
    print("\n")
