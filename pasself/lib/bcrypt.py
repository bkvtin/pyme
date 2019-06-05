#!/usr/bin/env python3

'''
using crypto aes to encrypt file
need to provide key with format to decrypt file and proceed
information after that

i've refered it from 
  - https://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes
  - https://stackoverflow.com/questions/3470546/python-base64-data-decode
'''

from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key, key_size=128):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)


def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)


'''
how to use
--

key = "{: <32}".format("<ur-plaintext-key>").encode("utf-8")
encrypt_file("<ur-file>", key)
decrypt_file("<ur-encrypt-file>", key)
'''