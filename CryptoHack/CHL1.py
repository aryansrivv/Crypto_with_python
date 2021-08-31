#CryptoHack level 1
final_flag = ''
flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for i in range (len(flag)):
    final_flag+=chr(flag[i])
print(final_flag)    
