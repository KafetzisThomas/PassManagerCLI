#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##################################################################################################################################
######################################################### PassManagerCLI #########################################################
##################################################################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
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
### GitHub:   https://github.com/KafetzisThomas/PassManagerCLI
###
### License:  GPL-3.0
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug. You should inspect the code yourself.
version = "1.2.0"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("Importing Standard Libraries...")
# Import standard libraries
import os, sys, platform, getpass
from datetime import datetime
from sqlite3 import OperationalError

print("Importing Script Modules...")
# Import module files
from Scripts.database import (
    insert_data_to_items,
    create_connection,
    print_items_data,
    update_items_data,
    delete_data,
    get_current_master_password,
    close_connection,
)
from Scripts.login import sign_up, sign_in, change_master_password
from Scripts.utils import generate_password
from Scripts.models import Item

print("Importing Third-Party Modules...")
# Import other (third-party) libraries
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

# Run check on python version, must be 3.6 or higher because of f strings
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    print(
        "Error Code U-2: This program requires running python 3.6 or higher! You are running"
        + str(sys.version_info[0])
        + "."
        + str(sys.version_info[1])
    )
    input("Press Enter to exit...")
    sys.exit()

# Check system platform to set correct console clear command
clear_command = "cls" if platform.system() == "Windows" else "clear"
os.system(clear_command)  # Clear console

############################################## MAIN ##############################################

print(
    f"\n{Fore.LIGHTYELLOW_EX}======================= PassManagerCLI v{version} ======================="
)
print("========= https://github.com/KafetzisThomas/PassManagerCLI ==========")
print("====================== Author: KafetzisThomas =======================")
print("\nFunction: Allows you to securely manage your saved passwords")
print("                     of your online accounts.")
print(
    f"\n> Enter {Fore.LIGHTBLUE_EX}Ctrl+C{Fore.RESET} to {Fore.LIGHTRED_EX}quit/cancel operation"
)
print(f"> Note that your typing is {Fore.LIGHTGREEN_EX}hidden{Fore.RESET}")

if not os.path.exists("vault.db"):
    conn, cur = create_connection()
    sign_up(conn, cur, Fore)
else:
    conn, cur = create_connection()
    sign_in(cur, Fore)


def menu():
    print(
        f"> Enter {Fore.LIGHTBLUE_EX}Ctrl+C{Fore.RESET} to {Fore.LIGHTRED_EX}quit/cancel operation\n"
    )
    print(
        f"--------------- {Fore.LIGHTYELLOW_EX}Menu Options{Fore.RESET} -------------------------------"
    )
    print(f"\t1. Add Item - {Fore.LIGHTBLUE_EX}Generate/Save{Fore.RESET} passwords")
    print(
        f"\t2. View {Fore.LIGHTMAGENTA_EX}Vault{Fore.RESET} - See your {Fore.LIGHTRED_EX}saved passwords{Fore.RESET}"
    )
    print(
        f"--------------- {Fore.LIGHTYELLOW_EX}Other Options{Fore.RESET} ------------------------------"
    )
    print(f"\t3. Check & Download Package {Fore.LIGHTGREEN_EX}Updates")
    print(f"\t4. {Fore.LIGHTCYAN_EX}Change{Fore.RESET} Master password")

    try:
        choice = int(input("\nChoice (1-4): "))
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTRED_EX}Exiting...{Fore.RESET}")
        sys.exit()

    if choice == 1:
        length = 12
        include_digits = None
        include_special_chars = None
        try:
            length = int(input("\nEnter password length (8-16): "))
            include_digits = input(
                f"Do you want to include digits? {Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}: "
            )
            include_special_chars = input(
                f"Do you want to include special chars? {Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}: "
            )
            if not (length >= 8 and length <= 16):
                print(
                    f"{Fore.LIGHTRED_EX}Password length is not within the specified limits.\n"
                )
                menu()
            if include_digits.lower() == "n":
                include_digits = False
            if include_special_chars.lower() == "n":
                include_special_chars = False
        except ValueError as err:
            print(f"{Fore.LIGHTRED_EX}{err}\n")
            menu()
        except KeyboardInterrupt:
            print(f"\n{Fore.LIGHTRED_EX}Operation cancelled.\n")
            menu()
        finally:
            password = generate_password(
                length,
                include_digits=include_digits,
                include_special_chars=include_special_chars,
                include_letters=True,
            )

        def main():
            try:
                name = input("\nName: ")
                username = input("Username: ")
                website = input("Website: ")
                notes = input("\nNote: ")

                if name and username and website != "":
                    item = Item(
                        name=name,
                        date_posted=datetime.now(),
                        website=website,
                        username=username,
                        password=password,
                        notes=notes,
                    )
                    insert_data_to_items(conn, cur, item)
                    print(
                        f"{Fore.LIGHTRED_EX}Information saved successfully into your vault.\n"
                    )
                else:
                    print(f"{Fore.LIGHTRED_EX}You did not fill all the fields.")
                    main()
            except KeyboardInterrupt:
                print(f"\n{Fore.LIGHTRED_EX}Operation cancelled.\n")
                menu()

        try:
            print(
                f"\nYour new password is: {Back.LIGHTBLUE_EX}{Fore.WHITE} {password} "
            )
            print(
                f"\n> Type {Fore.LIGHTGREEN_EX}y{Fore.RESET} to save the above password. {Back.LIGHTGREEN_EX}{Fore.BLACK} Highly Recommended! "
            )
            print(
                f"> Type {Fore.LIGHTRED_EX}n{Fore.RESET} to create a password by your own."
            )
            print(
                f"> Enter {Fore.LIGHTBLUE_EX}Ctrl+C{Fore.RESET} to {Fore.LIGHTRED_EX}cancel{Fore.RESET} this operation."
            )

            save = input(
                f"\nDo you want to save that password? {Fore.GREEN}y{Fore.RESET}/{Fore.RED}n{Fore.RESET}: "
            )
            if save.lower() == "y":
                main()
                menu()
            elif save.lower() == "n":
                print(
                    f"> Use 8 or more characters with a mix of {Fore.LIGHTGREEN_EX}letters{Fore.RESET}, {Fore.LIGHTGREEN_EX}numbers{Fore.RESET} & {Fore.LIGHTGREEN_EX}symbols{Fore.RESET}.\n"
                )
                password = input("Password: ")
                if password != "":
                    main()
                    menu()
                else:
                    print(f"{Fore.LIGHTRED_EX}You did not fill all the fields.\n")
                    menu()
            else:
                print(f"{Fore.LIGHTRED_EX}Undefined choice.\n")
                menu()
        except KeyboardInterrupt:
            print(f"\n{Fore.LIGHTRED_EX}Operation cancelled.\n")
            menu()

    elif choice == 2:
        print_items_data(cur)

        def vault_options():
            print(
                f"\n\n> Enter {Fore.LIGHTBLUE_EX}Ctrl+C{Fore.RESET} to {Fore.LIGHTRED_EX}quit/cancel operation\n"
            )
            print(
                f"--------------- {Fore.LIGHTYELLOW_EX}Vault Options{Fore.RESET} ------------------------------"
            )
            print(f"\t1. Refresh {Fore.LIGHTBLUE_EX}Vault{Fore.RESET}")
            print(f"\t2. {Fore.LIGHTRED_EX}Delete{Fore.RESET} a record")
            print(f"\t3. Update {Fore.LIGHTRED_EX}record{Fore.RESET} info")

            try:
                choice = int(input("\nChoice (1-3): "))
                if choice == 1:
                    print_items_data(cur)
                    vault_options()
                elif choice == 2:
                    print_items_data(cur)
                    # Ask user for which record (ID) of the row want data to be deleted
                    delete_record = input(
                        "\n\nWhich specific record (name) do you want to delete from the vault?\n> "
                    )
                    delete_data(conn, cur, delete_record)
                    print(f"{Fore.LIGHTRED_EX}Record ID Successfully deleted.")
                    vault_options()
                elif choice == 3:
                    print_items_data(cur)

                    # Ask user for which record (name) of the row want data to be updated
                    update_record = input(
                        f"\n\nWhich specific {Fore.LIGHTRED_EX}record (name){Fore.RESET}"
                        f" do you want to {Fore.LIGHTBLUE_EX}update{Fore.RESET} from the vault?\n> "
                    )

                    # Ask user for name of the column to change value in row
                    colName = input(
                        f"\nWhich specific {Fore.LIGHTCYAN_EX}column name{Fore.RESET}"
                        f" do you want to update from the {Fore.LIGHTMAGENTA_EX}vault{Fore.RESET}?"
                        "\n\t(name, username, password, website, notes)\n> "
                    ).lower()

                    # Ask user for new value
                    colValue = input(
                        f"\nWrite {Fore.LIGHTBLUE_EX}new{Fore.RESET} item:\n> "
                    ).strip()

                    update_items_data(conn, cur, colName, colValue, update_record)
                    print(f"{Fore.LIGHTRED_EX}Information Successfully updated.")
                    vault_options()
                else:
                    print(f"{Fore.LIGHTRED_EX}Undefined choice.")
                    vault_options()
            except ValueError as err:
                print(f"{Fore.LIGHTRED_EX}{err}")
                vault_options()
            except OperationalError:
                print(f"{Fore.LIGHTRED_EX}Record ID not found.")
                vault_options()
            except KeyboardInterrupt:
                print(f"\n{Fore.LIGHTRED_EX}Operation canceled.\n")
                menu()

        vault_options()

    elif choice == 3:
        # Update required packages to the latest versions if exist
        print("\nChecking for available package updates...")
        os.system("pip install --upgrade -r requirements.txt")
        print("\nAll required packages are up to date.")
        input("Press Enter to get back to the Menu...")
        os.system(clear_command)  # Clear console
        menu()

    elif choice == 4:
        old_master_username = input("\nOld Master Username: ")
        master_username = input("New Master Username: ")
        master_password = getpass.getpass("New Master Password: ").encode("utf-8")
        if (
            get_current_master_password(cur, old_master_username)
            and master_username != ""
        ):
            change_master_password(
                conn, cur, old_master_username, master_username, master_password
            )
            print(
                f"{Fore.LIGHTRED_EX}Master username & password successfully updated.\n"
            )
        else:
            print(f"{Fore.LIGHTRED_EX}Master username not found.\n")
        menu()

    else:
        print(f"{Fore.LIGHTRED_EX}Undefined choice.\n")
        menu()

    close_connection(conn)


if __name__ == "__main__":
    menu()
