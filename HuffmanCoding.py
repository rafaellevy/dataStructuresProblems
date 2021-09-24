import sys
from collections import Counter

class Node:
    def __init__(self, value, key):
        self.key = key
        self.value = value

class HuffNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) //2
        while currentIdx > 0 and heap[currentIdx].value < heap[parentIdx].value:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
    
    def remove(self):
        self.swap(0, len(self.heap) -1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) -1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
    

def buildHuffTree(array):
    # MinHeap object
    min_heap = MinHeap(array)
    hoff_tree = []

    while len(min_heap.heap) > 1:
        # remove the root node of heap
        node1 = min_heap.remove()
        # remove the root node of heap
        node2 = min_heap.remove()
        node3 = HuffNode(node1.value + node2.value)
        node3.left = node1
        node3.right = node2
        hoff_tree.append(node3)
        min_heap.insert(node3)

    print([x.value for x in hoff_tree])

    




def huffman_encoding(data):
    #counter returns a dictionary 
    counter = dict(Counter(data))
    frequencyArray = []
    for key, value in counter.items():
        node = Node(value, key)
        frequencyArray.append(node)
    for node in frequencyArray:
        print(node.key, node.value)
    print()

    print()
    buildHuffTree(frequencyArray)

huffman_encoding("AAATBBSIS")

def huffman_decoding(data,tree):
    pass
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
    print ("The content of the encoded data is: {}\n".format(decoded_data))
"""

    