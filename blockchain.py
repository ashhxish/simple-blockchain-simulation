import hashlib
import time
class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    

    def create_genesis_block(self):
        return Block(0, "0", ["Genesis Block"])
    
   
    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
           
            if current_block.hash != current_block.calculate_hash():
                return False
        
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

   
    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Transactions: {block.transactions}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Current Hash: {block.hash}")
            print("")

def proof_of_work(block, difficulty=4):
    target = '0' * difficulty
    while block.hash[:difficulty] != target:
        block.timestamp += 1  
        block.hash = block.calculate_hash()
    return block


if __name__ == "__main__":
   
    blockchain = Blockchain()
    
    blockchain.add_block(["Transaction 1", "Transaction 2"])
    blockchain.add_block(["Transaction 3", "Transaction 4"])

    last_block = blockchain.chain[-1]
    mined_block = proof_of_work(last_block)
    blockchain.chain[-1] = mined_block  

    blockchain.display_chain()

   
    if blockchain.validate_chain():
        print("Blockchain is valid!")
    else:
        print("Blockchain is invalid!")
    
    
    blockchain.chain[1].transactions = ["Tampered Transaction"]
    if blockchain.validate_chain():
        print("Blockchain is valid!")
    else:
        print("Blockchain is invalid!")
