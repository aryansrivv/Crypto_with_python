#!/usr/bin/python
from random import randint

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char)+s-65) % 26 + 65)
        elif (char == " "):
            result += " "
        else :
            result += chr ((ord(char)+s-97) % 26 + 97)
    return result

text = input ("Enter the plaintext")
print("Key is random")
s = randint(0,26)

print "Plain Text : " + text
print "Shift pattern : " + str(s)
print "Cipher: " + encrypt (text,s)
