# Pass_Manager

__A Password Manager created with Python for saving your critical login information. It is very lightful and easy to use,
designed for the best hardware performance.__

## Getting Started

### With this software you can...

1. Store your critical passwords including usernames, emails and urls of your favourite login forms!
================================================================
2. Generate safe passwords for your future online accounts!
================================================================
3. See your vault inside a terminal (CLI) menu!
================================================================

## Built With

- [Cryptography 37.0.2](https://pypi.org/project/cryptography/) for vault encryption (a safe and updated module of python that does the work done).
* Database File -> data.db

----------------------------------------------------------------------------------------------------------------------------------

- [Hashlib](https://pypi.org/project/hashlib/) for the login system protection, specifically it comes with sha256 type of encryption. 
* The login information are stored in 'credentials.txt' file.

----------------------------------------------------------------------------------------------------------------------------------

## Installation

### - How to Download:

-  __Download Automatically__:  Click the [download](https://github.com/KafetzisThomas/Pass_Manager/archive/refs/heads/main.zip) link on the right.

-----------------------------------------------------------------------------------------------------------------------------------

-  __Download Manually__: Open the terminal on your machine and type the following command:

```
git clone https://github.com/KafetzisThomas/Pass_Manager.git
```

-----------------------------------------------------------------------------------------------------------------------------------

- Use the package manager [pip](https://pip.pypa.io/en/stable) to install the requirements.txt from your terminal!

```
pip install -r requirements.txt
```

## Usage

The only thing you have to do is to run the '__main.py__' file in your terminal and all thats it!

__Windows:__
``` python main.py ```
__Mac/Linux:__
``` ./main.py ```
* __For Mac/Linux:__ Make sure you made it executable with the following command:
```
chmod +x main.py
```

## For Security Reasons

__You need to overwrite the default __username__ and __password__ using the 'Sign Up' form that it is included in the software.__

* Default Username > __user__
* Default Password > __pass__

## Files Explained

- 'createdb.py' file is for the database creation (File -> data.db). 
  There will be your usernames, passwords, emails, urls of your accounts in an encrypted format.
- 'encrypt.py' file is for the process of encryption is needed to the database table, so nobody can access your information without the login credentials.
- 'decrypt.py' file is for the process of decryption is needed to the database table, so you can see your passwords inside the software.
- 'generateKey.py' creates automatically a file including your unique universal key of entering your login information, without this you cannot enter into your vault.
- 'login.py' is for the login form that appears at the startup of the software.
  **This also reads the 'generateKey.py' file to match the details from the user.
- 'dataprinting.py' is for the printing decryption information from the database table inside the software. 
  **This also reads the 'decrypt.py' file in condition to decrypt the data. (encrypted data -> decrypted data -> print decrypted data)
- 'dataentry.py' is for the encrypted data importation to the database table.
- 'credentials.txt' is for saving the username and password (encrypted) to be readable in 'login.py' file.

## Author

- __KafetzisThomas__

## Bug Reports

**If you find any bugs in the code, do not hesitate to make a pull request! 🤓**