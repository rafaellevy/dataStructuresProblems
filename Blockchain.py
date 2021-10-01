import hashlib
import datetime
 
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.to_hash = str(timestamp) + data + str(previous_hash)
        self.hash = self.calc_hash(self.to_hash)
        
    def calc_hash(self, to_hash):
        sha = hashlib.sha256()
        
        # Need to change the hash_str
        # hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(to_hash.encode('utf-8'))
        # print(sha.hexdigest())
        return sha.hexdigest()
        
    
class BlockChain:
    def __init__(self):
        # the head will stay constant -- it will point to the genesis block            
        self.head = None
        # the tail will point the most recently added Node  -- the 'end'  so everything points back to the genesis block (the first block ever)
        self.tail = None
        
    def add_block(self, block):
        if self.head is None:
            self.head = block
        if self.tail is None:
            self.tail = block
        elif self.tail is not None:
            block.previous_hash = self.tail.hash
            self.tail = block



# Created first/genesis block
timestamp = datetime.datetime.now()
data = 'Genesis Block'
"""
to_hash = str(timestamp) + data
sha = hashlib.sha256()
sha.update(to_hash.encode('utf-8'))
previous_hash = sha.hexdigest()
# print(previous_hash)
"""
testBlock = Block(timestamp, data, 0)

# Create blockchain
blockchain = BlockChain()

# add block to empty blockchain
blockchain.add_block(testBlock)

# add another block with the same timestamp as the genesis block
data_second_block = 'Second Block'
# second_block must take previous hash
second_block = Block(timestamp, data_second_block, testBlock.hash)
blockchain.add_block(second_block)

# add third block with the same timestamp and data as the second block
third_block = Block(timestamp, data_second_block, second_block.hash)
blockchain.add_block(third_block)


print("The previous hash (second block):", third_block.previous_hash)
print("The hash (third block):", third_block.hash)
print("The data and time (third block):", third_block.data, third_block.timestamp)
print()
print("The previous hash (first block):", second_block.previous_hash)
print("The hash (second block):", second_block.hash)
print("The data and time (second block):", second_block.data, second_block.timestamp)
print()
print("The previous hash (no previous block):", testBlock.previous_hash)
print("The hash (first/genesis block):", testBlock.hash)
print("The data and time (first/genesis block):", testBlock.data, testBlock.timestamp)
    


#Hello Rafael, you made great work so far.
"""First, if my answer is helpful Please mark it as accepted.
Your code is good and well organized.
But you need to add at least three test cases with two edge cases .
Add one edge case with new object if the block is empty and add another with new object if the timestamp is the same.
If you still have anything else please let me know.
Best wishes."""