import hashlib

def sign_up():
    print("\n********** Sign Up **********")
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
        print("You have registered successfully!")
    else:
        print("The password is not the same as above!\n")

def sign_in():
    print("\n********** Login System **********")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    authenticate = password.encode()
    authenticate_hash = hashlib.md5(authenticate).hexdigest()

    with open("credentials.txt", "r") as f:
        stored_username, stored_password = f.read().split("\n")
    f.close()
    if username == stored_username and authenticate_hash == stored_password:
         print("Logged in Successfully!")
    else:
         print("Login failed!\n")
         sign_in()