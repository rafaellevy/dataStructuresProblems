import sys
from collections import Counter
import time
 
start = time.time()
 
class HoffNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        
class Node:
    def __init__(self, value, key):
        self.key = key
        self.value = value
        
        
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
 
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx +1)):
            self.siftDown(currentIdx, len(array) -1, array)
        return array
        
 
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx].value < heap[childOneIdx].value:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
 
            if heap[idxToSwap].value < heap[currentIdx].value:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
 
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i] 
        
    def remove(self):
        # this function assumes that there is more than one item in the list. 
        
        # switch root node and last node
        self.swap(0, len(self.heap) -1, self.heap)
        # print([x.value for x in self.heap])
        removed = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        # print([x.value for x in self.heap])
        return removed
    
    def insert(self, new_node):
        self.heap.append(new_node)
        self.siftUp(len(self.heap) - 1, self.heap)
        
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx].value < heap[parentIdx].value:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
def buildHoffTree(array):
        
        min_heap = MinHeap(array)
        hoff_tree = []
        while len(min_heap.heap) > 1:
            node1 = min_heap.remove()
            node2 = min_heap.remove()
            node3 = HoffNode(node1.value + node2.value)
            node3.left = node1
            node3.right = node2
            hoff_tree.append(node3)
            min_heap.insert(node3)
            # hoff_list.append(removed)
            
        # print([x.value for x in min_heap.heap])
        # print([x.value for x in hoff_tree])
        
        """
        for node in hoff_tree:
            print("Node's value: ", node.value)
            try: 
                print("Node's left child's value & key: ", node.left.value, node.left.key)
                print("Node's right child's value & key: ", node.right.value, node.right.key)
            except: 
                print("Node's left child's value: ", node.left.value)
                print("Node's right child's value: ", node.right.value)
            print()
        """
            
        return hoff_tree
 
 
def huffman_encoding(data):
    
    #counter returns a dictionary 
    counter = dict(Counter(data))
    frequencyArray = []
    for key, value in counter.items():
        node = Node(value, key)
        frequencyArray.append(node)
   
    # minHeap = MinHeap(frequencyArray)
    
    # print([x.value for x in minHeap.heap])
    hoff_tree = buildHoffTree(frequencyArray)
    
    # With our list of nodes (the hoff_tree), we need to assign bit codes for each letter. 
    # left child is 0
    # right child is 1
    # make a for loop that checks each parent to see if they have children, and if those children are of class Node
    # if the child is of class node, we can assign it the binary value
    # make a dict first
    
    binary_code = {}
    # start at the root node
    # start binary count
    cur_node = hoff_tree[-1]
    binary_prefix = ''
    
    traverse_tree(cur_node, binary_code, binary_prefix)
    # print(binary_code)
    
    encoded_message = ''
    for letter in data:
        encoded_message += binary_code[letter]
        
    return encoded_message, hoff_tree
    
def traverse_tree(node, binary_code, binary_prefix):
    if isinstance(node, Node):
        """
        print(node.value, node.key)
        print(binary_prefix)
        print()
        """
        binary_code[node.key] = binary_prefix
    else:
        if node.left is not None:
            traverse_tree(node.left, binary_code, binary_prefix + "0")
        if node.right is not None:
            traverse_tree(node.right, binary_code, binary_prefix + "1")
        
def huffman_decoding(data,tree):
    data += 'x'
    decoded_message = ''
    cur_node = tree[-1]
    # print(start_node.value)
    for bit in data:
        if isinstance(cur_node, Node):
            decoded_message += cur_node.key
            cur_node = tree[-1]
        
        if bit == '0':
            cur_node = cur_node.left
        elif bit == '1':
            cur_node = cur_node.right
                
    return decoded_message
 
"""
result = huffman_encoding("AAATBBSIS")
print(result[0])
huffman_decoding(result[0], result[1])
"""
 
 
if __name__ == "__main__":
    codes = {}
 
    a_great_sentence = "The bird is the word"
 
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
 
    encoded_data, tree = huffman_encoding(a_great_sentence)
 
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
 
    decoded_data = huffman_decoding(encoded_data, tree)
 
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
 
end = time.time()
 
print(f'the program took {end - start} time.')
# 0.0013794898986816406
# is 1.72 times faster