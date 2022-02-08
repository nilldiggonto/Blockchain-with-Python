from web3 import Web3
infura_url = 'https://mainnet.infura.io/v3/a40993e45c414eb8b1e6d6a4afc7650c'

webt =  Web3(Web3.HTTPProvider(infura_url))
print(webt.isConnected())

current_block_number = webt.eth.blockNumber
print(current_block_number)

balance = webt.eth.getBalance('TokenEtherAccount')

print(balance) #wei

# wei conversion
ether_balance =webt.fromWei(balance,'ether')
print(ether_balance)