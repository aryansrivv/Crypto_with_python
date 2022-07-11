# use lines 2 ,3 
#from pwn import xor 
#xor("label",13)

# for manual 

l= 'label'
s1 = []
for i in range (len(l)):
    a = ord(l[i])
    b = a^13
    s1.append(b)
s2 = []
for i in range (len(l)):
    x = chr(s1[i])
    s2.append(x)
final = ''
for i in s2 :
    final += i 
 print (final)   
