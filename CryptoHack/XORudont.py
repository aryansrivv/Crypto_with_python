#This one is pretty tircky one 
# message^secret_key = flag 
# we know that flag has 'crypto{' for sure .
# so message^secret_key^flag[:6] = 0 
# message^secret_key^flag[:6]^secret_key[:6] = secret_key[:6]
# message^flag[:6] = secret_key[:6]

from pwn import xor 
a = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
b = bytes.fromhex(a)
c = 'crypto{'

d= xor (b,c)

# d comes out to be myXORke ---> must be myXORkey , repeat this for to be equal or greater than the length of the message 

d = 'myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey'
flag = xor ( b , d )
print (flag)
