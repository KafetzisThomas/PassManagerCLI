#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##################################################################################################################################
########################################################## Pass_Manager ##########################################################
##################################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Function: Allows you to securely manage your saved passwords of your online accounts.
###
### NOTES:    1. Required Third-Party Packages: [pysqlitecipher],[cryptography],[colorama]
###                 >>> See the Readme for instructions on how to install them.
###
###           2. I am a total amateur at programming so if something doesn't work I'll try to fix it but might not
###                 even know how, so don't expect too much.
###
### Author:   KafetzisThomas
###
### GitHub:   https://github.com/KafetzisThomas/Pass_Manager
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug. You should inspect the code yourself.
version = "1.2.0"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("Importing Standard Libraries...")
# Import standard libraries
import os, sys, time, string, secrets, platform
print("Importing Script Modules...")
# Import module files
import Scripts.database as db
print("Importing Third-Party Modules...")
# Import other (third-party) libraries
import colorama
from colorama import Fore as F, Back as B
colorama.init(autoreset=True)

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

print(f"\n{F.LIGHTYELLOW_EX}======================= Pass_Manager v{version} =======================")
print("========= https://github.com/KafetzisThomas/Pass_Manager ==========")
print("===================== Author: KafetzisThomas ======================")
print("\nFunction: Allows you to securely manage your saved passwords")
print("                     of your online accounts.")
print(f"\n> Enter {F.LIGHTBLUE_EX}Ctrl+C{F.RESET} to {F.LIGHTRED_EX}quit/cancel operation")
print(f"> Note that your typing is {F.LIGHTGREEN_EX}hidden{F.RESET}")
db.set_database()

# Menu Options
def menu():
    print(f"> Enter {F.LIGHTBLUE_EX}Ctrl+C{F.RESET} to {F.LIGHTRED_EX}quit/cancel operation\n")
    print(f"--------------- {F.LIGHTYELLOW_EX}Menu Options{F.RESET} -------------------------------")
    print(f"\t1. Add Item - {F.LIGHTBLUE_EX}Generate/Save{F.RESET} passwords")
    print(f"\t2. View {F.LIGHTMAGENTA_EX}Vault{F.RESET} - See your {F.LIGHTRED_EX}saved passwords{F.RESET}")
    print(f"--------------- {F.LIGHTYELLOW_EX}Other Options{F.RESET} ------------------------------")
    print(f"\t3. Check & Download Package {F.LIGHTGREEN_EX}Updates")
    print(f"\t4. {F.LIGHTCYAN_EX}Change{F.RESET} Master password")
    
    try:
        choice = input("\nChoice (1-4): ")
    
    except KeyboardInterrupt:
        print(f"\nExiting in {F.LIGHTRED_EX}5{F.RESET} seconds...")
        time.sleep(5)
        sys.exit()
    
    # Generate a secure password
    if choice == "1":
        try:
            # Define the alphabet
            letters, digits, special_chars = string.ascii_letters, string.digits, string.punctuation
            alphabet = (letters + digits + special_chars)

            # Set password length
            pwd_length = int(input("\nEnter password length: "))

            # Generate a password string
            password = ''
            for i in range(pwd_length):
                password += ''.join(secrets.choice(alphabet))
        
        except ValueError as err:
            print(f"{F.LIGHTRED_EX}{err}\n")
            menu()
        except KeyboardInterrupt:
            print(f"\n{F.LIGHTRED_EX}Operation cancelled.\n")
            menu()

        def main():
            try:
                # Get input from the user and store information inside the database table (vault)
                name = input("\nName: ")
                username = input("Username: ")
                website = input("Website: ")
                note = input("\nNote: ")
                
                if name and username and website != '':
                    db.insert_data(name, username, password, website, note)
                    print(f"{F.LIGHTRED_EX}Information Saved Successfully into your Vault.\n")
                else:
                    print(f"{F.LIGHTRED_EX}You did not fill all the fields.")
                    main()
            
            except KeyboardInterrupt:
                print(f"\n{F.LIGHTRED_EX}Operation cancelled.\n")
                menu()

        try:
            # Print the generated password
            print(f"\nYour new password is: {B.LIGHTBLUE_EX}{F.WHITE} {password} ")
            print(f"\n> Type {F.LIGHTGREEN_EX}y{F.RESET} to save the above password. {B.LIGHTGREEN_EX}{F.BLACK} Highly Recommended! ")
            print(f"> Type {F.LIGHTRED_EX}n{F.RESET} to create a password by your own.")
            print(f"\n*Enter {F.LIGHTBLUE_EX}Ctrl+C{F.RESET} to {F.LIGHTRED_EX}cancel{F.RESET} this operation.\n")
            
            # Option for saving the generated password
            save = input(f"Do you want to save that password? {F.GREEN}y{F.RESET}/{F.RED}n{F.RESET}: ")
            
            # Save the generated password if user filled the required fields
            if save.lower() == "y":
                main()
                menu()
            elif save.lower() == "n":
                # Let user create a password by his own
                print(f"> Use 8 or more characters with a mix of {F.LIGHTGREEN_EX}letters{F.RESET}, {F.LIGHTGREEN_EX}numbers{F.RESET} & {F.LIGHTGREEN_EX}symbols{F.RESET}.\n")                
                password = input("Password: ")
                
                if password != '':
                    main()
                    menu()
                else:
                    print(f"{F.LIGHTRED_EX}You did not fill all the fields.\n")
                    menu()
            
            else:
                print(f"{F.LIGHTRED_EX}Undefined choice.\n")
                menu()
        
        except KeyboardInterrupt:
            print(f"\n{F.LIGHTRED_EX}Operation cancelled.\n")
            menu()

    elif choice == "2":
        db.print_data()       
        
        def vault_options():
            print(f"\n\n> Enter {F.LIGHTBLUE_EX}Ctrl+C{F.RESET} to {F.LIGHTRED_EX}quit/cancel operation\n")
            print(f"--------------- {F.LIGHTYELLOW_EX}Vault Options{F.RESET} ------------------------------")
            print(f"\t1. Refresh {F.LIGHTBLUE_EX}Vault{F.RESET}")
            print(f"\t2. {F.LIGHTRED_EX}Delete{F.RESET} a record")
            print(f"\t3. Update {F.LIGHTRED_EX}record{F.RESET} info")
            
            try:
                choice = input("\nChoice (1-3): ")
                
                if choice == "1":
                    db.print_data()
                    vault_options()
                elif choice == "2":
                    db.print_data()
                    db.delete_data()
                    print(f"{F.LIGHTRED_EX}Record ID Successfully deleted.")
                    vault_options()
                elif choice == "3":
                    db.print_data()
                    db.update_data()
                    print(f"{F.LIGHTRED_EX}Information Successfully updated.")
                    vault_options()
                else:
                    print(f"{F.LIGHTRED_EX}Undefined choice.")
                    vault_options()
            
            except ValueError as err:
                print(f"{F.LIGHTRED_EX}{err}")
                vault_options()
            except RuntimeError as err:
                print(f"{F.LIGHTRED_EX}Record ID not found.")
                vault_options()
            except KeyboardInterrupt:
                print(f"\n{F.LIGHTRED_EX}Operation canceled.\n")
                menu() 
        
        vault_options()

    elif choice == "3":
        # Update required packages to the latest versions if exist
        print("\nChecking for available package updates...")
        os.system("pip install --upgrade -r requirements.txt")
        print("\nAll required packages are up to date.")
        input("Press Enter to get back to the Menu...")
        
        # Clear console
        os.system(clear_command)
        menu()

    elif choice == "4":
        db.change_master_password()
        menu()
    
    else:
        print(f"{F.LIGHTRED_EX}Undefined choice.\n")
        menu()

menu()
