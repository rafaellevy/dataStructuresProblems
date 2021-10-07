### Huffman Coding

I made a dictionary to store the frequency for each character.
I used a list to represent the priority queue so I could use the pop and sorted method.
I used a list to represent the HuffmanTree so I could keep track of the parent
nodes for traversing it.

The time complexity will be O(nlogn) because the sorted method takes O(nlogn).
The space complexity is O(n), because the data structure size depends on the size
of the input.
