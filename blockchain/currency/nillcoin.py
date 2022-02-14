import datetime as _dt
import hashlib as _hash
import json
from urllib import response
import requests
from uuid import uuid4
from urllib.parse import urlparse


class Blockchain:
    def __init__(self):
        self.chain = []
        #transactions before create block
        self.transactions = []
        #Create Block
        self.create_block(proof=1,previous_hash='0')
        #nodes
        self.nodes = set()

    #block creation
    def create_block(self,proof,previous_hash):
        block = {
            'index':len(self.chain)+1,
            'timestamp':str(_dt.datetime.now()),
            'proof':proof,
            'previous_hash':previous_hash,
            'transactions':self.transactions 
            }
        self.transactions = []
        self.chain.append(block)
        return block

    #Get Previous block
    def get_previous_block(self):
        return self.chain[-1]

    #Proof of work
    def proof_of_work(self,previous_proof):
        new_proof = 1
        check_proof= False

        while check_proof is False:
            hash_operation = _hash.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof +=1
        return new_proof

    #hash function
    def hash(self,block):
        encoded_block = json.dumps(block,sort_keys=True).encode()
        return _hash.sha256(encoded_block).hexdigest()

    #chain validation
    def is_chain_valid(self,chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = _hash.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index +=1
        return True

    # Transactions
    def add_transaction(self,sender,receiver,amount):
        transaction_data = {
            'sender':sender,
            'receiver':receiver,
            'amount':amount,
        }
        self.transactions.append(transaction_data)
        previous_block = self.get_previous_block()
        return previous_block['index']+1

    # node
    def add_node(self,address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    # replace chain
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)

        for node in network:
            response = requests.get(f'http://{node}/chains')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False

    


