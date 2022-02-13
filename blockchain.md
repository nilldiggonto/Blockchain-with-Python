* Blockchain
    ```
    genesis_block: {
        data: dict,list,tuple,whatever,
        prev_hash: 00000,
        own_hash: 000AA
    },
    second_block:{
        data: dict,list,tuple,whatever,
        prev_hash: 000AA,
        own_hash: 222AA,
    },
    third_block:{
        data: dict,list,tuple,whatever,
        prev_hash: 222AA,
        own_hash: 333AA,
    }
    ```

* SHA256 HASH (secure hash algorithm 256 bytes)
    * hexadecimal hash
    * It's like Fingerprint but for any Digital Documents

    * Requirements for hash
        * One-Way (must be unique)
        * Deterministic (Same data same hash)
        * Fast Computation
        * Avalanche Effect (Even a tiny change of data,Whole hash will change)
        * Withstand collisions (If rarely two different data got same hash,It will create collisions) 
    
* Immutable Ledger
    * You can't change block in the chain

* Distributed p2p network
    * Proble to solve
        * change the whole blockchain
        * accidental data loss
    * Copies the full blockchain ledger to all the network (Distribute p2p)

* Mining
    * nonce gives the flexibility to mine new block
    * nonce++ , it's a increment count from the previous blocks
    * after 5th block, 6th block will have nonce number= 5+1
    ```
    block_n:{
        nonce:4,
        data:{
            transaction_1: 20tk,
            transaction_2:30tk,
        },
        prev_hash: 222AA,
        own_hash: 444AA
    }

    ```
    * To mine a certain hash miners must meet a target or less than target
        * if a hash is 24SSDFG........
        * and the target is 000
        * miners hash should 000234235... not 0023423..... (leading 3 zeros)

        * Robust Example
            * if nonce 24 is the lastest block
            * the target hash must contain three leading zeros
            * next nonce will something that can be hashable with three leading zeros
            * so miners will have to brute force to find a nonce, that generate hash with three leading zeros

* Byzantine fault tolerance
    * In a decentralize system if one system fails the algorith check if all the other systems working or not and come to a conclusion rather than shutting down the whole system for one fault.

* Consensus Protocol
    * Attackers (Spam block at the end of block)
    * Competing chains (mine blocks but fail to add end of the block)

    * Types of consensus protocol
        * Proof-of-work (pow)
        * proof-of-stakes (pos)
        * other