from fastapi import FastAPI,HTTPException
from intro_blockchain import blockchain as _blockchain

blockChain = _blockchain.BlockChain()
app = FastAPI()

def validateBlockChain():
    return blockChain.is_chain_valid()
       
@app.get('/validate')
def validateChain():
    return blockChain.is_chain_valid()

#mine api
@app.post('/test/mine_block/')
def mineBlock(data:str):
    if not validateBlockChain():
        return HTTPException(status_code=400,detail="Invalid BlockChain")
    block = blockChain.mine_block(data=data)
    return block

#Full BlockChain
@app.get('/test/block/list/')
def blockList():
    if not validateBlockChain:
        return HTTPException(status_code=400,detail="Invalid BlockChain")
    chain = blockChain.chain
    return chain

@app.get('/previous/block/')
def previous_block():
    if not validateBlockChain:
        return HTTPException(status_code=400,detail="Invalid BlockChain")
    
    return blockChain.get_previous_block()

