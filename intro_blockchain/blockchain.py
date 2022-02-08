"""
Genesis Block (the first block of a blockchain)
{
    id:0,
    proof:1,
    previous_hash: "0"
}-> hashing (123AA)

{
    id:1,
    proof:2,
    previous_hash: "123AA"
}-> new hash (234AA)
"""
import datetime as _dt
import hashlib as _hashlib
from itertools import chain
import json as _json
from operator import index

class BlockChain:

    def __init__(self)->None:
        print('inititate')
        self.chain = list()
        genesis_block = self._create_block(data="genesis",proof=1,previous_hash="0",index=0)
        print(genesis_block)
        self.chain.append(genesis_block)
        print(self.chain)

    def mine_block(self,data:str)->dict:
        previous_block = self.get_previous_block()
        print(previous_block)
        previous_proof = previous_block['proof']
        index          = len(self.chain) + 1
        proof          = self._proof_of_work(previous_proof,index,data)
        previous_hash  = self._hash(block=previous_block)
        block          = self._create_block(data=data,proof=proof,previous_hash=previous_hash,index=index)
        self.chain.append(block)
        return block
        

    def _hash(self,block)->str:
        encoded_block = _json.dumps(block,sort_keys=True).encode()
        return _hashlib.sha256(encoded_block).hexdigest()

    def _to_digest(self,new_proof:int,previous_proof:int,index:int,data:str)-> bytes:
        to_digest = str(new_proof ** 2 -previous_proof ** 2 + index) + data
        return to_digest.encode()

    def _proof_of_work(self,previous_proof:int,index:int,data:str)->int:
        new_proof = 1
        check_proof = False

        while not check_proof:
            print(new_proof)
            to_digest = self._to_digest(new_proof=new_proof,previous_proof=previous_proof,index=index,data=data)
            has_value = _hashlib.sha256(to_digest).hexdigest()

            if has_value[:4] == "0000":
                check_proof = True
            else:
                new_proof +=1
        return new_proof

    def get_previous_block(self)->dict:
        print(self.chain)
        return self.chain[-1]

    def _create_block(self,data:str,proof:int,previous_hash:str,index:int) -> dict:
        print('created')
        block = {
            "index":index,
            "timestamp": str(_dt.datetime.now()),
            "data":data,
            "proof":proof,
            "previous_hash":previous_hash
        }
        return block
