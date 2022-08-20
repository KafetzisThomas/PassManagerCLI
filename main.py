from os import path
import time
import string
import random
import createdb
import generateKey
import dataentry
import dataprinting
import login
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print("""
====================== Pass_Manager =======================
=== https://github.com/KafetzisThomas/Pass_Manager.git ====
======== Thomas Kafetzis - Github: KafetzisThomas =========
-----------------------------------------------------------

1.Sign Up
2.Login
3.Exit

""")

def access():
    try:
        choice = int(input(":"))
        time.sleep(0.10)
        if choice == 1:
            login.sign_in()
            time.sleep(0.10)
            login.sign_up()
            time.sleep(0.10)
            login.sign_in()
        elif choice == 2:
            time.sleep(0.10)
            login.sign_in()
            time.sleep(0.10)
        elif choice == 3:
            print("Program closed.") 
            exit()
        else:
            print("Undefined choice.")
            access()
    except ValueError:
        print("ValueError: Use only numbers.")
        access()
access()

def menu():
 print ("""
---------- Menu------------
1.Generate/Save Password
2.View Saved Password
3.Exit
---------------------------

""")

 option = input(":")
 time.sleep(0.10)

 if option == "1":
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
    if(path.exists('data.db')==False):
        generateKey.generateKey()
        createdb.create_database()
    time.sleep(0.10)
    exit = int(input("Enter 0 if you want to exit or 1 to continue entring data: "))
    while(exit==1):
        time.sleep(0.10)
        username = input("Username: ")
        time.sleep(0.10)
        email = input("Email: ")
        time.sleep(0.10)
        url = input("Url: ")
        time.sleep(0.10)
        dataentry.enter_data("Username: " + username,"Password: " + password,"Email: " + email,"Url: " + url)
        exit = int(input("Enter 0 if you want to exit or 1 to continue entering data: "))
        print("\nInformation stored successfully into the vault!\n")

  time.sleep(0.10)
  print(f"\nYour new password is: {Fore.GREEN}{password}")
  time.sleep(0.10)
  save = input("Do you want to save that password? y/n: ")
  if save.lower() == "y":
     main()
     menu()
  else:
    print("Undefined choice.")
    time.sleep(0.10)
    menu()

 if option == "2":
    time.sleep(0.10)
    print("\n======== My Vault ========")
    dataprinting.print_data()
    time.sleep(1.0)
    menu()
 if option == "3":
    print("Program closed.")
    exit()
menu()