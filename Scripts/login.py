from Scripts.database import insert_data_to_credentials, get_master_password, update_credentials_data
from Scripts.user import User
import getpass, bcrypt, sys


def sign_up(conn,cur, Fore):
    try:
        master_username = input("\nMaster Username: ")
        master_password = getpass.getpass("Master Password: ").encode('utf-8')
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTRED_EX}Exiting...{Fore.RESET}")
        sys.exit()

    if master_username != '':
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(master_password, salt)
        user = User(master_username, hashed_password)
        insert_data_to_credentials(conn, cur, user)
        print(f"\n> User created {Fore.LIGHTGREEN_EX}successfully")


def sign_in(cur, Fore):
    try:
        master_username = input("\nMaster Username: ")
        master_password = getpass.getpass("Master Password: ").encode('utf-8')
        stored_master_username = get_master_password(cur, master_username)
        stored_master_password = get_master_password(cur, master_username)
        if master_username == stored_master_username[0] and bcrypt.checkpw(master_password, stored_master_password[1]):
            print(f"\n> Welcome back, {Fore.LIGHTGREEN_EX}{master_username}")
        else:
            print(f"{Fore.RED}Incorrect credentials.")
            sys.exit()
    except TypeError:
        print(f"{Fore.RED}Incorrect credentials.")
        sys.exit()
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTRED_EX}Exiting...{Fore.RESET}")
        sys.exit()


def change_master_password(conn, cur, old_master_username, master_username, master_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(master_password, salt)
    update_credentials_data(conn, cur, old_master_username, master_username, hashed_password)
