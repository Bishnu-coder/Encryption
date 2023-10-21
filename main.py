from Encrypt_Decrypt import *

inp = input("Enter text to be encrypted\n-> ")

KEY = 19
enc = Encrypt(inp, KEY)

print("\nStarting Encryption ...")
if enc.encryptedMessage is not None:
    Encrypted = enc.get_encrypted()
    print(f"encrypted text of {inp} is\n-> {Encrypted} \n")
else:
    Encrypted = None

print("\nStarting Decryption ...")
dec = Decrypt(Encrypted)
if dec.encryptedMessage is not None:
    Decrypted = dec.get_decrypted()
    print(f"decrypted text of {Encrypted} is\n-> {Decrypted} ")

