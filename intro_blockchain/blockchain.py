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
        # print(genesis_block)
        self.chain.append(genesis_block)
        # print(self.chain)

    def mine_block(self,data:str)->dict:
        previous_block = self.get_previous_block()
        # print(previous_block)
        previous_proof = previous_block['proof']
        index          = previous_block['index'] + 1
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
            # print(new_proof)
            to_digest = self._to_digest(new_proof=new_proof,previous_proof=previous_proof,index=index,data=data)
            has_value = _hashlib.sha256(to_digest).hexdigest()

            if has_value[:4] == "0000":
                check_proof = True
            else:
                new_proof +=1
        return new_proof

    def get_previous_block(self)->dict:
        # print(self.chain)
        return self.chain[-1]

    def _create_block(self,data:str,proof:int,previous_hash:str,index:int) -> dict:
        # print('created')
        block = {
            "index":index,
            "timestamp": str(_dt.datetime.now()),
            "data":data,
            "proof":proof,
            "previous_hash":previous_hash
        }
        return block

    def is_chain_valid(self) -> bool:
        
        block_index     =   1
        current_block   =   self.chain[0]

        while block_index < len(self.chain):
            next_block = self.chain[block_index]
            if next_block['previous_hash'] != self._hash(current_block):
                return False
            
            previous_proof = current_block['proof']
            next_index,next_data,next_proof = next_block['index'],next_block['data'],next_block['proof']
            hash_value = _hashlib.sha256(self._to_digest(new_proof=next_proof,previous_proof=previous_proof,index=next_index,data=next_data)).hexdigest()
            if hash_value[:4] != "0000":
                return False 
            block_index += 1
            current_block = next_block
        return True

