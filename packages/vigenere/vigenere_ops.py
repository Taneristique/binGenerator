from string import ascii_lowercase as al 
class vigenere:
    """It is main class which is the parent of all following vigenere classes."""
    def __init__(self,text,index):
        self.vig=[[*(al[i:]+al[:i])] for i in range(len(al))]
        self.index=index
        self.text=text
        if self.text=='' or self.text is None:
            raise ValueError("Text parameter cannot be empty or null!")
    @staticmethod
    def indexer(text:str)->int:
        return [ord(c)%97 for c in text] #ord('a')=97
class decode_vigenere(vigenere):
    def __init__(self,text,index='default'):
        super().__init__(text,index)
        rest=self.solve(text=self.text,key=self.indexer(index))
        print(rest)
    def solve(self,text:str,key:list[int]=[])->str:
        """
        This  method gets two parameters which are text and key than decodes given text data that is encoded by vigenere encryption algorithm with or without key parameter which is empty by default. solve("mom{opzglk_vpialk}",indexer("tht"))
        'tht{vigner_cipher}'.
        :param text: it is vigenere encoded text.
        :param indexer:it is the list of integers which is the key to encrypt and decrypt text.
        """
        i,res,k=0,'',len(key)
        for c in text:
            if c not in al:
                res+=c 
                continue 
            res+=al[self.vig[key[i%k]].index(c)]
            i+=1
        return res 
class encode_vigenere(vigenere):
    def __init__(self, text, index):
        super().__init__(text, index)
        result=self.encrypt(text=self.text,key=self.indexer(index))
        print(result)
    def encrypt(self,text:str,key:list[int]=[])->str:
        i,res,k=0,'',len(key)
        for c in text:
            if c not in al:
                res+=c 
                continue
            res+=self.vig[key[i]][ord(c)%97] 
            i+=1
            if i==k:
                i=0
        return res 
def encode():
    txt=input('Please provide a text\n')
    seed=input('Please provide a seed\n')
    encode_vigenere(txt,seed)
def decode():
    txt=input('Please provide a text\n')
    seed=input('Please provide a seed\n')
    decode_vigenere(txt,seed)  