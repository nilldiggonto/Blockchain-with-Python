* Crypto World
    * Technology (Blockchain)
    * Protocol/Coin(Bitcoin protocol simply let bitcoin users to communicate each other;waves,neo,ripple,ethereum)
    * Token (smart contract build by protocol)

* Bitcoin system
    * Nodes (Device people use but not mining)
    * Miners (People who mine)
    * Large Miners 
    * Mining Pools

* Bitcoin Monetary
    * The Halving 
    * Block Frequency

* Mining Difficulty
    * Current Target
        * How many leading zeros
        * What's the probability of creating valid block
    * Calculate Difficulty
        * Change leading zeros to get more difficulty

* Mining Pool
    * Help to mine for individual miner.

* Nonce Range
    * Some Issue
        * 32-bit number
        * Integer (0~4billion)
    * For individual miner(let 40 sec to go through 4billion hashes)
        * Solution to Nonce Range
            * unix timestamp
    * For Mining pool(let 0.2ms it can go through trillion hashes)
        * Solution to mining pool nonce range
            * Miner Transactions
            * Mempool (memory pool)
                * pick another transaction with highest fees 
                * change block configuration

* Mempools
    * Transaction
    * Every individual or node has a mempool
    * Not a blockchain, staging process before add to block
    
* Orphan block
    * wait till some block added to confirm transaction

* 51% attack
    * Hash Rate Attack not a hacker
    

    