from packages.utf8 import bytesToUtf8 as bytetof8 
from packages import bytesToHex as bytHex
from packages.vigenere.vigenere_ops import encode as vencode
from packages.vigenere.vigenere_ops import decode as vdecode
from packages.utf8.decryptFile import decryption 
from packages.utf8.encryptFile import UTF_8FileToBytes

print("  aaaa"," \t  iii                          gggggggggggggggggg              \n"
      "   aa","  \t  iii                          gggg                                 \n"
      "   aa","  \t                               gggg  ","           \teeeeeeeee         nnnnnnnnn\n"
      "   aaaaaaa", "\t iiiii   nnnnnnnnnn            bbbb     gggggggg     ","\teee   eee\t  nnn   nnn\n"
      "   aa   aa","\t  iii    nnnn  nnnn            gggg         gggg","\teeeeeeeee         nnn   nnn\n"
      "   aa   aa","\t  iii    nnnn  nnnn            bbbb         gggg","\teee               nnn   nnn\n"
      "   aaaaaaa","\t iiiii   nnnn  nnnn            ggggggggggggggggg    ","\teeeeeeeee         nnn   nnn \t\t By TaNeRiStIqUe")
def UTF8_toPleinTextFile():
    chose=input("Would you want to encrypt or decrypt your file write DECRYPT or ENCRYPT \n")
    file_location=input("Write the location of required file : ")
    writeFile=input("Would you want to create a new file(optional)? Write Yes or No : ")
    writeFile=True if writeFile=="Yes" else  False
    encryptedFileName=input("What will be the name of encrypted file(Optional)? : " if chose=="ENCRYPT" else "What will be the name of decrypted file(Optional)? : ") 
    if chose=="ENCRYPT":
        UTF_8FileToBytes(file_location=file_location,writeFile=writeFile,encryptedFileName=encryptedFileName)
    else:
        decryption(file_location=file_location,writeFile=writeFile,encryptedFileName=encryptedFileName)



def menu():
    print("Menu\n1.Encode UTF-8 to Bytes\n2.Decode Bytes to UTF-8\n3.Decode or Encode a txt or bin file data via UTF-8 encryption protocol\n4.Convert Bytes To Hex\n5.Convert Hex to Bytes\n6.Encode a plain-text via vigenere chipher\n7.Decode Vigenere Chipher\n")
    action={"1":bytetof8.encoding,"2":bytetof8.decoding,"3":UTF8_toPleinTextFile,"4":bytHex.byteTHex,"5":bytHex.hexTbyte,"6":vencode,"7":vdecode}
    chose=input()
    action[chose]()
menu()

