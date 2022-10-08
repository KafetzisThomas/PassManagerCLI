#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################################################################
########################################### Pass_Manager ##############################################
#######################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
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
###           3. I am a completelly amateur at programming so if something doesn't work I'll try to fix it but might not
###                even know how, so don't expect too much.
###
### Author:   KafetzisThomas
###
### GitHub:   https://github.com/KafetzisThomas/Pass_Manager
###
### License:  GPL-3.0
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug. You should inspect the code yourself.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("Importing Standard Libraries...")
# Importing standard libraries
from os import path
import os, sys, time, string, random
print("Importing Script Modules...")
# Importing module files
import Scripts.createdb as createdb
import Scripts.generateKey as generateKey
import Scripts.dataentry as dataentry
import Scripts.dataprinting as dataprinting
import Scripts.login as login
print("Importing Third-Party Modules...")
# Importing other (third-party) libraries
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print("Checking for available package updates...")
# Updating required packages to the latest versions if exist
os.system("pip install --upgrade -r requirements.txt")
os.system("cls")

# Run check on python version, must be 3.6 or higher because of f strings
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    print("Error Code U-2: This program requires running python 3.6 or higher! You are running" + str(sys.version_info[0]) + "." + str(sys.version_info[1]))
    input("Press Enter to exit...")
    sys.exit()

###################################### MAIN ##############################################

print(f"""{Fore.LIGHTYELLOW_EX}
====================== Pass_Manager ======================={Fore.RESET}
{Fore.GREEN}=== https://github.com/KafetzisThomas/Pass_Manager.git ====
================= Author: KafetzisThomas ==================
-----------------------------------------------------------
{Fore.LIGHTYELLOW_EX}
<< Login >>{Fore.RESET}
1.Sign Up
2.Sign In
3.Exit{Fore.LIGHTYELLOW_EX}
-----------
""")

# Login form
def access():
    try:
        choice = int(input(":"))
        time.sleep(0.10)
        if(choice==1):
            login.sign_in()
            time.sleep(0.10)
            login.sign_up()
            time.sleep(0.10)
            login.sign_in()
        elif(choice==2):
            time.sleep(0.10)
            login.sign_in()
            time.sleep(0.10)
        elif(choice==3):
            print(f"{Fore.RED}Program closed.") 
            sys.exit()
        else:
            print(f"{Fore.RED}Undefined choice.")
            access()
    except ValueError as err:
        print(f"{Fore.RED}{err}")
        access()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program closed.")
        sys.exit()
access()

def menu():
    print(f"""{Fore.LIGHTYELLOW_EX}
---------- Menu------------{Fore.RESET}
1.Generate/Save Password
2.View Saved Passwords
3.Exit{Fore.LIGHTYELLOW_EX}
---------------------------
""")
    
    try:
        option = input(":")
        time.sleep(0.10)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program closed.")
        sys.exit()
    
    # Generating a secure password
    if(option=="1"):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
            
        time.sleep(0.10)
        length = int(input("Enter password length: "))
        random.shuffle(characters)
        passw = []
        for i in range(length):
            passw.append(random.choice(characters))
            random.shuffle(passw)
                
            password = "".join(passw)

        def main():
            try:
                # Checking if 'data.db' file exists
                if(path.exists('data.db')==False):
                    # Generating a universal key if it doesn't exist
                    generateKey.generateKey()
                    # Creating a database if it doesn't exist
                    createdb.create_database()
                time.sleep(0.10)
                # Option to continue/stop entring data
                exit = int(input(f"Enter {Fore.GREEN}0{Fore.RESET} if you want to exit or {Fore.GREEN}1{Fore.RESET} to continue entring data: "))
                while(exit==1):
                    # Getting input from the user before storing information inside the database table (VAULT)
                    time.sleep(0.10)
                    name = input("Name: ")
                    time.sleep(0.10)
                    username = input("Username: ")
                    time.sleep(0.10)
                    website = input("Website: ")
                    time.sleep(0.10)
                    dataentry.enter_data(f"Name: {Fore.GREEN}{name}",f"Username: {Fore.GREEN}{username}",f"Password: {Fore.GREEN}{password}",f"Website: {Fore.GREEN}{website}")
                    # Option to continue/stop entring data
                    exit = int(input(f"Enter {Fore.GREEN}0{Fore.RESET} if you want to exit or {Fore.GREEN}1{Fore.RESET} to continue entring data: "))
                    time.sleep(0.10)
                    print(f"\n{Fore.RED}*Information stored successfully into your vault!")
                else:
                    time.sleep(0.10)
            except ValueError as err:
                print(err)
                main()

        time.sleep(0.10)
        # Printing out the generated password
        print(f"\nYour new password is: {Fore.GREEN}{password}")
        time.sleep(0.10)
        # Option for saving the generated password 
        save = input(f"Do you want to save that password? {Fore.LIGHTBLUE_EX}y/{Fore.RED}n{Fore.RESET}: ")
        if(save.lower()=="y"):
            main()
            menu()
        elif(save.lower()=="n"):
            time.sleep(0.10)
            menu()
        else:
            print(f"{Fore.RED}Undefined choice.")
            time.sleep(0.10)
            menu()

    if(option=="2"):
        time.sleep(0.10)
        print(f"\n{Fore.LIGHTYELLOW_EX}======== My Vault ========")
        # Printing out the data from the database table as decrypted
        dataprinting.print_data()
        time.sleep(0.10)
        menu()

    if(option=="3"):
        print(f"{Fore.RED}Program closed.")
        sys.exit()
    else:
        print(f"{Fore.RED}Undefined choice.")
        time.sleep(0.10)
        menu()
menu()