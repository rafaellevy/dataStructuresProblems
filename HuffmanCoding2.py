from os import error
import sys
from collections import Counter
from typing import Awaitable

class HuffNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key

def traverse_tree(node, binary_code, binary_prefix):
    if isinstance(node, Node):
        binary_code[node.key] = binary_prefix
    else:
        if node.left is not None:
            traverse_tree(node.left, binary_code, binary_prefix + "0")
        if node.right is not None:
            traverse_tree(node.right, binary_code, binary_prefix + "1")

def huffman_encoding(data):
    if data == "":
        data = "empty"
    counter = dict(Counter(data))
    frequencyArray = []
    for key, value in counter.items():
        node = Node(value, key)
        frequencyArray.append(node)

    pq = sorted(frequencyArray, key = lambda node : node.value, reverse=True)

    huff_tree = []

    while len(pq) > 1:
        node1 = pq.pop()
        node2 = pq.pop()
        node3 = HuffNode(node1.value + node2.value)
        node3.left = node1
        node3.right = node2
        huff_tree.append(node3)
        pq.append(node3)
        pq = sorted(pq, key = lambda node : node.value, reverse=True)

    binary_code = {}
    binary_prefix = ''
    traverse_tree(huff_tree[-1], binary_code, binary_prefix)
    # print(binary_code)

    encoded_message = ''
    for letter in data:
        encoded_message += binary_code[letter]
        # print(encoded_message)

    return encoded_message, huff_tree

def huffman_decoding(data, tree):
    data += 'x'
    decoded_message = ''
    cur_node = tree[-1]
    
    for bit in data:
        if isinstance(cur_node, Node):
            decoded_message += cur_node.key
            cur_node = tree[-1]
        if bit == '0':
            cur_node = cur_node.left
        elif bit == "1":
            cur_node = cur_node.right
    return decoded_message



# result = huffman_encoding("ASMOO")
if __name__ == "__main__":
    codes = {}

    # case 1
    a_empty_string = ""
    # case 2
    a_great_sentence = "The bird is the word"
    # case 3
    a_binary_string = "011100101"
    
    # before encoding check size and content 
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_empty_string)))
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_binary_string)))
    print ("The content of the data is: {}\n".format(a_empty_string))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    print ("The content of the data is: {}\n".format(a_binary_string))
    print()
    # case 1 encoding and decoding 
    encoded_data, tree = huffman_encoding(a_empty_string)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # expect the size and the content of the data to stay the same
    print()
    # case 2 encoding and decoding 
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # expect the size of the encoded data to be smaller
    print()
    # case 3 encoding and decoding 
    encoded_data, tree = huffman_encoding(a_binary_string)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # expect the size and the content of the data to stay the same





