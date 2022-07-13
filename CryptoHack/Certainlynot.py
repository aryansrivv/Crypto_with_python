# Open SSL use ( given to us was a DER-encoded x509 RSA certificate ) certp.der is the file 
# openssl x509 -in certp.der -inform der -text -noout
# you will get a modulus but its in hexadecimal , convert it to decimal 
# you can also use 
# openssl x509 -inform der -in certp.der

modulus_1 = '00:b4:cf:d1:5e:33:29:ec:0b:cf:ae:76:f5:fe:2d:c8:99:c6:78:79:b9:18:f8:0b:d4:ba:b4:d7:9e:02:52:06:09:f4:18:93:4c:d4:70:d1:42:a0:29:13:92:73:50:77:f6:04:89:ac:03:2c:d6:f1:06:ab:ad:6c:c0:d9:d5:a6:ab:ca:cd:5a:d2:56:26:51:e5:4b:08:8a:af:cc:19:0f:25:34:90:b0:2a:29:41:0f:55:f1:6b:93:db:9d:b3:cc:dc:ec:eb:c7:55:18:d7:42:25:de:49:35:14:32:92:9c:1e:c6:69:e3:3c:fb:f4:9a:f8:fb:8b:c5:e0:1b:7e:fd:4f:25:ba:3f:e5:96:57:9a:24:79:49:17:27:d7:89:4b:6a:2e:0d:87:51:d9:23:3d:06:85:56:f8:58:31:0e:ee:81:99:78:68:cd:6e:44:7e:c9:da:8c:5a:7b:1c:bf:24:40:29:48:d1:03:9c:ef:dc:ae:2a:5d:f8:f7:6a:c7:e9:bc:c5:b0:59:f6:95:fc:16:cb:d8:9c:ed:c3:fc:12:90:93:78:5a:75:b4:56:83:fa:fc:41:84:f6:64:79:34:35:1c:ac:7a:85:0e:73:78:72:01:e7:24:89:25:9e:da:7f:65:bc:af:87:93:19:8c:db:75:15:b6:e0:30:c7:08:f8:59'
modulus_2 = modulus_1.replace(":","")

# modulus_2 = '00b4cfd15e3329ec0bcfae76f5fe2dc899c67879b918f80bd4bab4d79e02520609f418934cd470d142a0291392735077f60489ac032cd6f106abad6cc0d9d5a6abcacd5ad2562651e54b088aafcc190f253490b02a29410f55f16b93db9db3ccdcecebc75518d74225de49351432929c1ec669e33cfbf49af8fb8bc5e01b7efd4f25ba3fe596579a2479491727d7894b6a2e0d8751d9233d068556f858310eee81997868cd6e447ec9da8c5a7b1cbf24402948d1039cefdcae2a5df8f76ac7e9bcc5b059f695fc16cbd89cedc3fc129093785a75b45683fafc4184f6647934351cac7a850e73787201e72489259eda7f65bcaf8793198cdb7515b6e030c708f859'

flag = int (flfg,16)
str(flag)
