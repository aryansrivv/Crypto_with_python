from pwn import xor 
f1 = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
f2 = bytes.fromhex(f1)
maybe_flag = ''
for i in range(256):
   maybe_flag1 =xor(f2,i)
   maybe_flag2 = str(maybe_flag1 ,'UTF-8')
   if 'crypto' in maybe_flag2:
        print (maybe_flag2)
        
#A decode error pops up tho , but the flag is also given as an output 
