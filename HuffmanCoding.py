import sys
from collections import Counter

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
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]   

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
    minHeap = MinHeap(frequencyArray)
    for node in minHeap.heap:
        print(node.key, node.value)

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

    