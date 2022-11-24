<h1 align="center">Pass_Manager</h1>

__What Is This?__ - Allows you to securely manage your saved passwords of your online accounts.

__How to Download:__ Click [here](https://github.com/KafetzisThomas/Pass_Manager/archive/refs/heads/main.zip) to download.

__Download Manually__: Open the terminal on your machine and type the following command:
```
git clone https://github.com/KafetzisThomas/Pass_Manager.git
```

Use [pip](https://pip.pypa.io/en/stable) to install the required packages:
```
pip install -r requirements.txt
```
___Make note that after installing the required packages, the software will be checking for package updates at every startup.___

## Built With

- [Cryptography](https://pypi.org/project/cryptography/) for vault encryption (a safe and constantly updated package that does the work done).
- [Hashlib](https://pypi.org/project/hashlib/) for the login system protection, specifically it comes with sha256 type of encryption. 

## Usage Notes - READ THIS

To use this script, run the ```Pass_Manager.py``` file in your terminal and that's it!

__Windows:__
``` python Pass_Manager.py ```
__Mac/Linux:__
``` ./Pass_Manager.py ```
* __For Mac/Linux:__ Make sure you make it executable with the following command:
```
chmod +x Pass_Manager.py
```

## For Security Reasons

__You need to overwrite the default __username__ and __password__ using the 'Sign Up' form that it is included in the software.__

* Default Username -> __user__
* Default Password -> __pass__

## IMPORTANT

I am a total amateur at programming so if something doesn't work I'll try to fix it but might not even know how, so don't expect too much. __I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.__ I tested it on my own and implemented some failsafes as best as I could, but there could always be some kind of bug. You should inspect the code yourself.

## Files Explained

- ```createdb.py``` file is for the database creation (File -> ```data.db```). There, will be your saved usernames, passwords, websites (URLs) of your accounts in an encrypted format.
- ```encrypt.py``` file is for the process of encryption is needed to the database table, so nobody can access your information without the login credentials.
- ```decrypt.py``` file is for the process of decryption is needed to the database table, so you can see your passwords inside the software.
- ```generateKey.py``` creates automatically a file including your unique universal key, without this you cannot enter into your vault.
- ```login.py``` is for the login form that appears at the startup of the software. This also reads the ```generateKey.py``` file to match the details from the user.
- ```dataprinting.py``` is to print the data from the database table as decrypted inside the software. This also reads the ```decrypt.py``` file in condition to decrypt the data. (encrypted data -> decrypted data -> print decrypted data)
- ```dataentry.py``` is for the encrypted data importation to the database table.
