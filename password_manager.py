import sys
sys.path.append(r'C:/Users/USER/AppData/Local/Programs/Python/Python312/Lib/site-packages')

import json, hashlib, os, pyperclip
from cryptography.fernet import Fernet

# Hashing master password

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexadigest()

    # Generating  key
    
    def generate_key():
        return Fernet.generate_key()

        # Initialize fernet cipher with the provided key

        def initialize_cipher(key):
            return Fernet(key)
            
            def encrypt_password(cipher, password):
                return cipher.encrypt(password.encode()).decode()

                # Decrypt passord

                def decrypt_password(cipher, encrypt_password):
                    return cipher.decrypt(encrypt_password.encode()).decode()

                    # register user

                    def register(username, master_password):

                        hashed_master_password = hash_password(master_password)
                        user_data ={'username' : username, 'master_password' : hashed_master_password }
                        file_name = 'user_data.json'

                        if os.path.exists(file_name) and os.path.getsize(file_name) == 0;
                        with open(file_name, 'w') as file :
                            json.dump(user_data, file)
                            print("\n[+] Registration done.... \n")
                            
                            else:
                                with open(file_name, 'x') as file:
                                    json.dump(user_data, file)
                                    print("\n[+] Registration done... \n")
                                    
                                    # Login function 
                                    def Login(username, entered_password):
                                        try:
                                            with open('user_data.json', 'r')
    
