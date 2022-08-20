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
            print(f"{Fore.RED}Program closed.") 
            exit()
        else:
            print(f"{Fore.RED}Undefined choice.")
            access()
    except ValueError as err:
        print(f"{Fore.RED}{err}")
        access()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program closed.")
        exit()
access()

def menu():
 print (f"""{Fore.LIGHTYELLOW_EX}
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
    exit()

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
    exit = int(input(f"Enter {Fore.GREEN}0{Fore.RESET} if you want to exit or {Fore.GREEN}1{Fore.RESET} to continue entring data: "))
    while(exit==1):
        time.sleep(0.10)
        username = input("Username: ")
        time.sleep(0.10)
        email = input("Email: ")
        time.sleep(0.10)
        url = input("Url: ")
        time.sleep(0.10)
        dataentry.enter_data("Username: " + Fore.GREEN + username,"Password: " + Fore.GREEN + password,"Email: " + Fore.GREEN + email,"Url: " + Fore.GREEN + url)
        exit = int(input(f"Enter {Fore.GREEN}0{Fore.RESET} if you want to exit or {Fore.GREEN}1{Fore.RESET} to continue entring data: "))
        time.sleep(0.10)
        print(f"\n{Fore.RED}*Information stored successfully into your vault!")

  time.sleep(0.10)
  print(f"\nYour new password is: {Fore.GREEN}{password}")
  time.sleep(0.10)
  save = input(f"Do you want to save that password? {Fore.LIGHTBLUE_EX}y/{Fore.RED}n{Fore.RESET}: ")
  if save.lower() == "y":
     main()
     menu()
  elif save.lower() == "n":
     time.sleep(0.10)
     menu()
  else:
    print(f"{Fore.RED}Undefined choice.")
    time.sleep(0.10)
    menu()

 if option == "2":
    time.sleep(0.10)
    print(f"\n{Fore.LIGHTYELLOW_EX}======== My Vault ========")
    dataprinting.print_data()
    print(f"{Fore.RED}\n*Your critical information are safe and protected!")
    time.sleep(1.0)
    menu()
 if option == "3":
    print(f"{Fore.RED}Program closed.")
    exit()
 else:
    print(f"{Fore.RED}Undefined choice.")
    time.sleep(0.10)
    menu()
menu()