def UTF_8FileToBytes(file_location,writeFile=False,encryptedFileName=""):    
    def encode(text):
        textLen=len(text)
        byteMaker=lambda index,array:bin(ord(array[index])).replace('0b','') #converts char to byte
        encryptedText=""
        encryptedData=[byteMaker(i,text) if len(byteMaker(i,text))==8 else (8-len(byteMaker(i,text)))*'0'+byteMaker(i,text) if len(byteMaker(i,text))<8 else '0x80'  for i in range(textLen)]
        for i in range(len(encryptedData)):
            encryptedText+=encryptedData[i]
        return encryptedText
    with open(file_location,mode="r") as text:
        txt=text.read()
        encryption=encode(txt)
    print(f"Plein text : {txt} \nEncrypted Text : {encode(txt)}" if '0x80' not in encryption else "Invalid Format Detected Please Check The File You Provided!")  
    if writeFile==True:
        with open(encryptedFileName,mode="w") as encrypt:
            encrypt.write(encryption)
    return 0
