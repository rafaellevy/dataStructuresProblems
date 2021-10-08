### LRU Cache

I chose to implement the LRU Cache with a doubly linked list (listofMostRecent), and hash table (cache) where the key is the same as the DoublyLinkedListNode id and the value is the DoublyLinkedListNode.

The doubly linked list was used
to keep track of the order of access (Most recently used node is head, and least
recently used is tail).  
Adding a new node is O(1) because it is added to the head of the linked list.  
If the capacity is full, removing the least recently used is O(1) because it is the tail.

The hash table was used to improve time complexity. Looking up the nodes from
the LRUCache becomes O(1).

In regard to the space complexity, it will be O(n) because the cache has a capacity.
