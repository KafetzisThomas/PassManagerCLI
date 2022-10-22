#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import hashlib, colorama, getpass
from colorama import Fore
colorama.init(autoreset=True)

# Creating a new user and a new password
def sign_up():
    print(f"""{Fore.LIGHTYELLOW_EX}
********** Sign Up **********{Fore.GREEN}
*Enter a new username and a new password.
*Note that your typing is hidden.\n""")
    # Asking the user for a username and a password
    # Get a hidden password input
    username = getpass.getpass("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    confirm_password = getpass.getpass("Confirm Password: ")
    # Checking if fields are filled
    # If this condition is True then the password will be encrypted
    if(username and password and confirm_password) != '' and (confirm_password==password):
        encode = confirm_password.encode()
        hash = hashlib.sha256(encode).hexdigest()

        # Saving the encrypted password in 'credentials.txt' file
        with open("credentials.txt", "w") as f:
             f.write(username + "\n")
             f.write(hash)
        f.close()
        print(f"{Fore.GREEN}You have registered successfully!")
    else:
        print(f"{Fore.RED}The password is not the same as above or you did not fill all the fields.")
        sign_up()

# Signing in with the existing credentials information
def sign_in():
    print(f"""{Fore.LIGHTYELLOW_EX}
********** Sign In **********{Fore.GREEN}
*Log in with your current username and password.
*Note that your typing is hidden.\n""")
    # Asking the user for the existing username and password
    # Get a hidden password input
    username = getpass.getpass("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    # Checking if fields are filled
    if(username and password) != '':
        # User input hashing for authentication
        authenticate = password.encode()
        authenticate_hash = hashlib.sha256(authenticate).hexdigest()

        # Reading the existing username and password from the 'credentials.txt' file
        with open("credentials.txt", "r") as f:
            stored_username, stored_password = f.read().split("\n")
        f.close()
        # Checking if user input credentials are the same as the saved ones
        if(username==stored_username) and (authenticate_hash==stored_password):
            print(f"Logged in as: {Fore.GREEN}{username}")
        else:
            print(f"{Fore.RED}Login failed!\nTry Again.")
            sign_in()
    else:
        print(f"{Fore.RED}You did not fill all the fields.")
        sign_in()