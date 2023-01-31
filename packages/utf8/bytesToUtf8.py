class bytesToUTF8:
    """This class only support UTF-8 and US-ASCII based inputs and encodes them to binary and decodes them to plein text. It has one parameter called encode which 
    is False by default.If encode is False this class will try to decode the given input,otherwise it will encode the given input.
     """
    def __init__(self,encode=False,file_location='',writeFile=False,encryptedFileName=""):
        pleinText=input() if encode==True else ''
        binInput=input() if encode==False else ''
        if encode==True and file_location!='' and writeFile==False:
            print("File is  encoding...")
            self.Encode(file_location)
        elif encode==True and file_location!="" and writeFile==True:
            encryptedFileName="defaultEncoding.txt" if encryptedFileName=="" else encryptedFileName
            print(f'File is encoding and saving on {file_location}...')
            self.Encode(file_location,writeFile,encryptedFileName)
        elif encode==False and file_location!="" and writeFile==False:
            print("File is decoding...")
            self.Decode(file_location)
        elif encode==False and file_location!="" and writeFile==True:
            encryptedFileName="defaultDecoding.txt" if encryptedFileName=="" else encryptedFileName
            print(f'File is decoding and saving on {file_location}...')
            self.Encode(file_location,writeFile,encryptedFileName)
        else:
            self.pleinText=pleinText if pleinText!='' else ''
            self.binInput=binInput if binInput!='' else ''
            self.Encode() if self.pleinText!='' else self.Decode() if self.binInput!='' else print('Please provide a value as input')
    def Encode(self,file_location='',writeFile=False,encryptedFileName=""):
        "Encodes plein text to UTF based bytes using ord function to get utf value of letter and bin function to convert utf value to binary."
        text='0b'
        encryptedText=''
        cmd=lambda t:bin(ord(t)).replace('0b','')
        encodedList=[cmd(text) if len(cmd(text))==8 else (8-len(cmd(text)))*'0'+cmd(text) if len(cmd(text))<8 else '00100000' for text in self.pleinText]
        encodedLen=len(encodedList)
        for i in range(encodedLen):
            encryptedText+=encodedList[i]
        print(encryptedText)
    def Decode(self,file_location="",writeFile=False,encryptedFileName=""):
        """Gets bytes and converts them to plein text using basic binary to int conversion and chr function.Only bytes must be provided to this method 
        otherwise the method will return inaccurate results or ValueError!""" 
        pleinTextOutput=''
        count=7
        num=0
        for i in range(len(self.binInput)):
            num+=pow(2,count)*int(self.binInput[i])
            pleinTextOutput+=chr(num) if count==0 else ''
            num=0 if count==0 else num
            count=7 if count==0 else count-1
        print(pleinTextOutput)
def encoding():
    e=bytesToUTF8(True)    
def decoding():
    d=bytesToUTF8()
