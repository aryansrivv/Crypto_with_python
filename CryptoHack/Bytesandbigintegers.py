from Crypto.Util.number import *
flag_in_base10 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag_in_hex = hex(flag_in_base10)
print (flag_in_hex)
initial = flag_in_hex[2:]
final_flag = bytes.fromhex(initial)
print(final_flag)
