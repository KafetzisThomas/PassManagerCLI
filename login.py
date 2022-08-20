import hashlib
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def sign_up():
    print(f"""{Fore.LIGHTYELLOW_EX}
********** Sign Up **********{Fore.GREEN}
*Enter a new username and a new password.\n""")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")
    if confirm_password == password:
        encode = confirm_password.encode()
        hash = hashlib.md5(encode).hexdigest()

        with open("credentials.txt", "w") as f:
             f.write(username + "\n")
             f.write(hash)
        f.close()
        print(f"{Fore.GREEN}You have registered successfully!")
    else:
        print(f"{Fore.RED}The password is not the same as above!")

def sign_in():
    print(f"""{Fore.LIGHTYELLOW_EX}
********** Sign In **********{Fore.GREEN}
*Log in with your current username and password.\n""")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    authenticate = password.encode()
    authenticate_hash = hashlib.md5(authenticate).hexdigest()

    with open("credentials.txt", "r") as f:
        stored_username, stored_password = f.read().split("\n")
    f.close()
    if username == stored_username and authenticate_hash == stored_password:
         print(f"Logged in as: {Fore.GREEN}{username}")
    else:
         print(f"{Fore.RED}Login failed!\nTry Again.")
         sign_in()