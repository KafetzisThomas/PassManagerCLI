#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##################################################################################################################################
########################################################## Pass_Manager ##########################################################
##################################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Function: Allows you to store your critical passwords including usernames, emails and websites (URLs) of your online accounts.
###
### NOTES:    1. For security reasons, you'll need to overwrite the default username and password using the 'Sign Up' form
###                                    that it is included in the software.		    	                     
###				            >>> See the Readme for instructions on this.
###
###           2. Required Third-Party Packages: [colorama],[cryptography]
###                         >>> See the Readme for instructions on how to install them.
###
###           3. I am a total amateur at programming so if something doesn't work I'll try to fix it but might not
###                even know how, so don't expect too much.
###
### Author:   KafetzisThomas
###
### GitHub:   https://github.com/KafetzisThomas/Pass_Manager
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug. You should inspect the code yourself.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("Importing Standard Libraries...")
# Import standard libraries
from os import path
import os, sys, time, string, random, platform
print("Importing Script Modules...")
# Import module files
import Scripts.createdb as createdb
import Scripts.generateKey as generateKey
import Scripts.dataentry as dataentry
import Scripts.dataprinting as dataprinting
import Scripts.login as login
print("Importing Third-Party Modules...")
# Import other (third-party) libraries
import colorama
from colorama import Fore as F, Back
colorama.init(autoreset=True)

print("Checking for available package updates...")
# Updating required packages to the latest versions if exist
os.system("pip install --upgrade -r requirements.txt")

# Check system platform to set correct console clear command
# Clear console
clear_command = "cls" if platform.system() == "Windows" else "clear"
os.system(clear_command)

# Run check on python version, must be 3.6 or higher because of f strings
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    print("Error Code U-2: This program requires running python 3.6 or higher! You are running" + str(sys.version_info[0]) + "." + str(sys.version_info[1]))
    input("Press Enter to exit...")
    sys.exit()

############################################## MAIN ##############################################

# Login Options
def access():
    print(f"\n{F.LIGHTYELLOW_EX}======================= Pass_Manager =======================")
    print("==== https://github.com/KafetzisThomas/Pass_Manager.git ====")
    print("================== Author: KafetzisThomas ==================")
    print("\nFunction: Allows you to store your critical passwords")
    print("             including usernames, emails and websites (URLs)")
    print("                 of your online accounts.")
    print(f"\n> Enter {F.BLUE}Ctrl+C{F.RESET} to {F.RED}quit/cancel operation")
    print(f"\n--------------- {F.YELLOW}Login Options{F.RESET} ------------------------------")
    print(f"\t1. Sign Up - Enter {F.LIGHTRED_EX}new{F.RESET} credentials")
    print(f"\t2. Sign In - Use your {F.LIGHTBLUE_EX}existing credentials")

    try:
        choice = input("\nChoice (1-2): ")
    except KeyboardInterrupt:
        print(f"\nExiting in {F.RED}5{F.RESET} seconds...")
        time.sleep(5)
        sys.exit()

    try:
        if(choice=="1"):
            login.sign_in()
            login.sign_up()
            login.sign_in()
        elif(choice=="2"):
            login.sign_in()
        else:
            print(f"{F.RED}Undefined choice.")
            access()
    except KeyboardInterrupt:
        print(f"\n{F.RED}Operation cancelled.")
        access()
access()

# Menu Options
def menu():
    print(f"> Enter {F.BLUE}Ctrl+C{F.RESET} to {F.RED}quit/cancel operation\n")
    print(f"--------------- {F.YELLOW}Menu Options{F.RESET} ------------------------------")
    print(f"\t1. Add Item - {F.LIGHTBLUE_EX}Generate/Save{F.RESET} passwords")
    print(f"\t2. View {F.LIGHTMAGENTA_EX}Vault{F.RESET} - See your {F.LIGHTRED_EX}saved passwords{F.RESET}")
    
    try:
        choice = input("\nChoice (1-2): ")
    except KeyboardInterrupt:
        print(f"\nExiting in {F.RED}5{F.RESET} seconds...")
        time.sleep(5)
        sys.exit()
    
    # Generate a secure password
    if(choice=="1"):
        try:
            characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

            length = int(input("\nEnter password length: "))
            random.shuffle(characters)
            passw = []
            for i in range(length):
                passw.append(random.choice(characters))
                random.shuffle(passw)
                    
                password = "".join(passw)
        except ValueError as err:
            print(f"{F.RED}{err}")
            menu()
        except KeyboardInterrupt:
            print(f"\n{F.RED}Operation cancelled.\n")
            menu()

        def main():
            try:
                # Check if 'data.db' file exists
                if(path.exists('data.db')==False):
                    # Generate a universal key if it doesn't exist
                    generateKey.generateKey()
                    # Create a database if it doesn't exist
                    createdb.create_database()

                # Get input from the user and store information inside the database table (Vault)
                name = input("\nName: ")
                username = input("Username: ")
                website = input("Website: ")
                note = input("\nNote: ")
                if(name and username and website) != '':
                    dataentry.enter_data(f"Name:     {F.GREEN}{name}",
                                        f"Username: {F.GREEN}{username}",
                                        f"Password: {F.RED}{password}",
                                        f"Website:  {F.GREEN}{website}",
                                        f"\nNote:     {F.LIGHTCYAN_EX}{note}")
                    
                    print(f"{F.RED}*Information Saved Successfully into your Vault!\n")
                else:
                    print(f"{F.RED}You did not fill all the fields.")
                    main()
            except KeyboardInterrupt:
                print(f"\n{F.RED}Operation cancelled.\n")
                menu()

        # Print the generated password
        print(f"\nYour new password is: {Back.GREEN}{F.BLACK} {password} ")
        # Option for saving the generated password 
        save = input(f"Do you want to save that password? {F.LIGHTBLUE_EX}y/{F.RED}n{F.RESET}: ")
        if(save.lower()=="y"):
            main()
            menu()
        elif(save.lower()=="n"):
            print(f"{F.RED}Operation cancelled.\n")
            menu()
        else:
            print(f"{F.RED}Undefined choice.\n")
            menu()

    if(choice=="2"):
        print(f"\n{F.LIGHTYELLOW_EX}================ My Vault ================")
        # Print the data from the database table as decrypted
        dataprinting.print_data()
        time.sleep(1)
        print("\n")
        menu()

    else:
        print(f"{F.RED}Undefined choice.\n")
        menu()
menu()