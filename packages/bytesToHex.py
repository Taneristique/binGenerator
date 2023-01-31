class BytesToHex:
    def __init__(self,convertToHex=False):
        byteString=input() if convertToHex==True else ''
        hexString=input() if convertToHex==False else ''
        self.bs=byteString if byteString!='' else ''
        self.hs=hexString if hexString!='' else ''
        self.hexToBytes() if convertToHex==False else self.bytesToHexa()
    def hexToBytes(self):
        hexValues={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
        bytes=""
        count=0
        self.hs=self.hs[::-1].upper() #reverse hex string
        for i in range(len(self.hs)):
            count+=hexValues[self.hs[i]]*pow(16,i) # decimal value of hexadecimal*16^(exponent)
        bytes+=bin(count).replace('0b','')
        print(bytes)
    def bytesToHexa(self):
        self.bs=self.bs[::-1]
        self.hexString=''
        num=0
        count=0
        for i in range(len(self.bs)):
            num+=int(self.bs[i])*pow(2,count)
            self.hexString+=hex(num)+'\t' if count==7 else ''
            num=0 if count==7 else num
            count=0 if count==7 else count+1
        print(self.hexString.split()[::-1])
def hexTbyte():
    h=BytesToHex()
def byteTHex():
    b=BytesToHex(True)