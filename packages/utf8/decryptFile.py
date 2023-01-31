def decryption(file_location,writeFile=False,encryptedFileName=""):
    plein_text=""
    with open(file_location) as file:
        file=file.read()
    nums=0
    counter=7
    for text in file:
        nums+=int(text)*pow(2,counter)
        plein_text+=chr(nums) if counter==0 else ''
        nums=0 if counter==0 else nums  
        counter=7 if counter==0 else counter-1
    if writeFile==True:
        with open(encryptedFileName,mode="w") as newFile:
            newFile.write(plein_text)
    print(f"Decription of {file_location} : {plein_text} {'is saved in'+encryptedFileName if encryptedFileName!='' else ''}")
        

    
    
    