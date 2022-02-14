from django.dispatch import receiver
from fastapi import Body, FastAPI, Response
from ..currency.nillcoin import Blockchain
from uuid import uuid4
from fastapi.param_functions import Body

app = FastAPI()

_blockchain = Blockchain()

node_address = str(uuid4()).replace('-','')


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
    #-- transaction
    transaction = _blockchain.add_transaction(sender=node_address,receiver='me',amount=1)
    return _blockchain.create_block(proof,previous_hash)

@app.post('/transaction',status_code=201)
async def add_transaction(request:dict=Body(...)):
    sender = request['sender']
    receiver = request['receiver']
    amount = request['amount']
    index = _blockchain.add_transaction(sender,receiver,amount)
    return {'message':f'Transaction {index} will be added'}

@app.get('/chains')
async def chain_list():
    return {'chain':_blockchain.chain,'length':len(_blockchain.chain)}

@app.get('/valid')
async def is_valid():
    is_valid =  _blockchain.is_chain_valid(_blockchain.chain)
    if is_valid:
        return {'info':'Blockchain is Valid'}
    return {'info':'Blockchain invalid'}

@app.post('/connect')
async def connect_node(request:dict=Body(...)):
    nodes = request['nodes']
    if nodes is None:
        return {'message':'no nodes added'}
    for node in nodes:
        _blockchain.add_node(node)
    return {'message':'Nodes Connected','total_nodes':nodes}

#replacing the chains with the longest one
@app.get('/replace/chain')
async def replace_chain():
    replace_chain = _blockchain.replace_chain()
    if not replace_chain:
        return {'message':'Chain still valid','actual_chain':_blockchain.chain}
    return {'message':'Chain Replaced','replace_chain':_blockchain.chain}



# uvicorn main:app --host 0.0.0.0 --port 80
# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')
#  uvicorn blockchain.app.main:app --host 127.0.0.1 --port 8000 --reload 