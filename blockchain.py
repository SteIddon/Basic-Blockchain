class Blockchain(object):
    def __init__(self):
    #chain list on first array, transactions stored in 2nd array
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)


    def new_block(self, proof, previous_hash=None):
    #this function creates new blocks and adds them to the existing chain
        pass
    #this method contains 2 parameters - proof & prev hash
        block = {
            'index': len(self.chain) + 1,
            'timestamp' : time(),
            'proof': proof,
            previous_hash: previous_hash or self.hash(self.chain[-1]),
        }
        #set the current transaction list to empty
        self.current_transactions=[]
        self.chain.append(block)
        return block

    def new_transaction(self):
    #this function adds transactions to the existing array
        pass
    #creates new transaction, sends 3 var to next block
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
        )
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
    #used for hashing blocks ## creates a SHA-256 block and orders the dictionairy
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()



    @property
    def last_block(self):
    #calls & returns last block in chain
        pass
    return self.chain[-1]

