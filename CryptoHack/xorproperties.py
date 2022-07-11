#given key 1 , and xor of key 2 ,3 
# just xor them you get xor of key 1 ,2 ,3 
# now xor it with the given flag^k1^k2^k3 you get flag^0 = flag 


key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key1_by = bytes.fromhex(key1)
key2 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
key2_by = bytes.fromhex(key2)
key12xor = xor(key1_by,key2_by)
key3 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
key3_by = bytes.fromhex(key3)
flag = xor (key12xor , key3_by)
print(flag)
