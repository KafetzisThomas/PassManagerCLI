#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import hashlib, colorama, getpass
from colorama import Fore as F
colorama.init(autoreset=True)

# Create a new user and a new password
def sign_up():
    print(f"\n{F.LIGHTYELLOW_EX}******************* Sign Up *********************")
    print(f"> Enter a NEW {F.GREEN}username{F.RESET} and a NEW {F.GREEN}password{F.RESET}.")
    print(f"> Note that your typing is {F.RED}hidden{F.RESET}.")
    # Ask the user for a username and a password
    # Get a hidden password input
    username = getpass.getpass("\nEnter Username: ")
    password = getpass.getpass("Enter Password: ")
    confirm_password = getpass.getpass("Confirm Password: ")
    # Check if fields are filled
    # If this condition is True then the password will be encrypted
    if(username and password and confirm_password) != '' and (confirm_password==password):
        encode = confirm_password.encode()
        hash = hashlib.sha256(encode).hexdigest()

        # Save the encrypted password in 'credentials.txt' file
        with open("credentials.txt", "w") as f:
             f.write(username + "\n")
             f.write(hash)
        f.close()
        print(f"{F.GREEN}You have registered Successfully!")
    else:
        print(f"{F.RED}The password is not the same as above or you did not fill all the fields.")
        sign_up()

# Sign in with the existing credentials information
def sign_in():
    print(f"\n{F.LIGHTYELLOW_EX}******************* Sign In *********************")
    print(f"> Log in with your current {F.GREEN}username{F.RESET} and {F.GREEN}password{F.RESET}.")
    print(f"> Note that your typing is {F.RED}hidden{F.RESET}.")
    # Ask the user for the existing username and password
    # Get a hidden password input
    username = getpass.getpass("\nEnter Username: ")
    password = getpass.getpass("Enter Password: ")
    # Check if fields are filled
    if(username and password) != '':
        # User input hashing for authentication
        authenticate = password.encode()
        authenticate_hash = hashlib.sha256(authenticate).hexdigest()

        # Read the existing username and password from the 'credentials.txt' file
        with open("credentials.txt", "r") as f:
            stored_username, stored_password = f.read().split("\n")
        f.close()
        # Check if user input credentials are the same as the saved ones
        if(username==stored_username) and (authenticate_hash==stored_password):
            print(f"\n> Logged in as: {F.GREEN}{username}")
        else:
            print(f"{F.RED}Incorrect username or password.")
            sign_in()
    else:
        print(f"{F.RED}You did not fill all the fields.")
        sign_in()