from Scripts.database import create_connection,create_credentials_table, create_items_table, insert_data_to_credentials, get_master_password, update_credentials_data
from Scripts.user import User
import getpass, bcrypt, sys
from Scripts.utils import load_encryption_key


def sign_up(F):
    conn, cur = create_connection()
    create_credentials_table(cur)
    create_items_table(cur)

    try:
        master_username = input("\nMaster Username: ")
        master_password = getpass.getpass("Master Password: ").encode('utf-8')
    except KeyboardInterrupt:
        print(f"\n{F.LIGHTRED_EX}Exiting...{F.RESET}")
        sys.exit()

    if master_username != '':
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(master_password, salt)
        user = User(master_username, hashed_password)
        insert_data_to_credentials(conn, cur, user)


def sign_in(F):
    conn, cur = create_connection()
    print(load_encryption_key(cur))
    try:
        master_username = input("\nMaster Username: ")
        master_password = getpass.getpass("Master Password: ").encode('utf-8')
        stored_master_username = get_master_password(cur, master_username)
        stored_master_password = get_master_password(cur, master_username)
        if master_username == stored_master_username[0] and bcrypt.checkpw(master_password, stored_master_password[1]):
            print(f"\n> Logged in {F.LIGHTGREEN_EX}Successfully")
        else:
            print(f"{F.RED}Incorrect credentials.")
            sys.exit()
    except TypeError:
        print(f"{F.RED}Incorrect credentials.")
        sys.exit()
    except KeyboardInterrupt:
        print(f"\n{F.LIGHTRED_EX}Exiting...{F.RESET}")
        sys.exit()

def change_master_password(conn, cur, old_master_username, master_username, master_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(master_password, salt)
    update_credentials_data(conn, cur, old_master_username, master_username, hashed_password)
