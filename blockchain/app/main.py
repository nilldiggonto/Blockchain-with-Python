from fastapi import FastAPI
from .blockchain import Blockchain

app = FastAPI()

_blockchain = Blockchain()

@app.get('/robots.txt')
async def robot():
    return '--'

@app.get('/')
async def index():
    return 'WELCOME TO BLOCKCHAIN'

@app.get('/mine')
async def mineBlock():
    previous_block = _blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = _blockchain.proof_of_work(previous_proof)
    previous_hash = _blockchain.hash(previous_block)
    return _blockchain.create_block(proof,previous_hash)

@app.get('/chains')
async def chain_list():
    return {'chain':_blockchain.chain,'length':len(_blockchain.chain)}

@app.get('/valid')
async def is_valid():
    is_valid =  _blockchain.is_chain_valid(_blockchain.chain)
    if is_valid:
        return {'info':'Blockchain is Valid'}
    return {'info':'Blockchain invalid'}
