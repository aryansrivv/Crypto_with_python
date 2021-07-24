#!/usr/bin/python

import base64


plaintext = input ("ENTER THE PLAINTEXT: \n")
plaintext_bytes = plaintext.encode("ascii")

encoded_data_bytes = base64.b64encode(plaintext_bytes)
encoded_data_string= encoded_data_bytes.decode("ascii")

print("Encoded text with base 64 is")
print(encoded_data_string)

decode_bytes = encoded_data_string.encode("ascii")
decoded_bytes = base64.b64decode(decode_bytes)
decoded_string = decoded_bytes.decode("ascii")
decision = input("DO YOU WANT TO DECODE IT BACK? (YES/NO)")
if (decision =="YES"):
    print(decoded_string)
