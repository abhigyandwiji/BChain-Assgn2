from block import Block
from time import time

class Blockchain():
    def __init__(self):
        self.blcno=2
        self.genesis_block=Block(1,00000000,000000000,"Dexter's Blockchain")
        self.blocks=[self.genesis_block]

    def get_last_hash(self):
        last_block=self.blocks[-1]
        last_hash=last_block.hash
        return (last_hash)
    
    def add_new_block(self,data,timestamp):
        prev_hash=self.get_last_hash()
        new_block=Block(self.blcno,prev_hash,timestamp,data)
        self.blcno+=1
        self.blocks.append(new_block)

    def get_last_timestamp(self):
        last_block=self.blocks[-1]
        last_hash=last_block.timestamp
        return (last_hash)