from packages.utf8 import encryptFile as u
from packages.utf8 import decryptFile as d
from packages.vigenere import vigenere_ops as vd
from packages.vigenere.vigenere_ops import encode
u.UTF_8FileToBytes("test.txt",True,"TestFile.bin")
u.UTF_8FileToBytes("test2.txt",True,"test2Encrypted.bin")
d.decryption("TestFile.bin",True,"TestFileDescription.txt")
vd.decode_vigenere(text="tivw",index="tht")
vd.decode_vigenere(text="tivw",index="tht")
vd.encode_vigenere(text="abcd",index="tht")
vd.decode_vigenere("mom{opzglk_vpialk}","tht")
vd.encode_vigenere(text="tht{vigner_cipher}",index="tht")
encode()