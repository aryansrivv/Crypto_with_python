#!/usr/bin/python


def revCipher(text):
    ciphertext = ""
    i = len(text)
    for l in range (i) :
        ciphertext = ciphertext + text[i-l-1]
    return ciphertext

text = input("ENTER THE TEXT:")
cipher = revCipher(text)
print ("cipher is %s" %(cipher))

plaintext= input("DO YOU WANT TO TRANSLATE IT BACK?(YES/NO) ")
if (plaintext == "YES"):
    print("plaintext is :%s"%(revCipher(cipher)))


