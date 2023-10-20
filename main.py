from Encrypt_Decrypt import *

inp = input("Enter text to be encrypted\n-> ")

KEY = 19
enc = Encrypt(inp, KEY)
Encrypted = enc.get_encrypted()
print(f"\nencrypted text Is\n-> {Encrypted} ")

dec = Decrypt(Encrypted)
Decrypted = dec.get_decrypted()
print(f"\ndecrypted text Is\n-> {Decrypted} ")

