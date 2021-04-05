from flask import Flask

class Blockchain(object):
    def __init__(self):
    #chain list on first array, transactions stored in 2nd array
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def proof_of_work(self, last_proof):
        #this is where consensus algorithm is implemented - self & last_proof paramaters
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof +=1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        #validating the block
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
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
        return self.chain[-1]

#creating node for app

app = Flask(__name__)
node_identifier = str(uuid4()).replace('-','')
#init blockchain
blockchain = Blockchain()
@app.route('/mine', methods=['GET'])
def mine():
    #making PoW algorithm
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    return "Mining new block"

    #rewarding the miner - 0 specifies new coin has been mined
    blockchain.new_transaction(
        sender="0",
        recipient = node_identifier,
        amount = 1,
    )
    #create block & add to chain -
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    response = {
        'message': "New block has been created",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    #checking if req data is present
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    #creating new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient', values['amount']])
    response = {'message': f'Transaction is scheduled to be added to Block No. {index}'}
    return jsonify(response), 201
    return "Adding a new Transaction"

@app.router('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)