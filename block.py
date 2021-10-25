from hashlib import blake2b, sha256

class Block():
    def __init__(self,blcno,prev,timestamp,data):
        self.blcno=blcno
        self.prev=prev
        self.nonce=0
        self.timestamp=timestamp
        self.hash=0
        self.data=data
        self.calculate_valid_hash()
    
    def is_hash_valid(self,hash):
        return (hash.startswith('0'*3))

    def calculate_valid_hash(self):
        hash=''
        nonce=0
        while(not self.is_hash_valid(hash)):
            temp=self.to_string()+str(nonce)
            hash=sha256(temp.encode()).hexdigest()
            nonce+=1

        self.nonce=nonce
        self.hash=hash

    def to_string(self):
        return "\nBlock No: \t{0}\nPrev Hash: \t{1}\nTimestamp: \t{2}\nNonce: \t\t{3}\nCurr Hash: \t{4}\nData: \t\t{5}\n\n".format(self.blcno,self.prev,self.timestamp,self.nonce,self.hash,self.data)