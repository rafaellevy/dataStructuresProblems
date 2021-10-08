class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        self.listOfMostRecent.setHeadTo(self.cache[key])
        return self.cache[key].value

    def set(self, key, value):
        if self.capacity <= 0:
            return -1
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.cache:
            if self.currentSize == self.capacity:
                keyToRemove = self.listOfMostRecent.tail.key
                self.listOfMostRecent.removeTail()
                del self.cache[keyToRemove]
                newNode = DoublyLinkedListNode(key, value)
                self.listOfMostRecent.setHeadTo(newNode)
                self.cache[key] = newNode
            elif self.currentSize < self.capacity:
                newNode = DoublyLinkedListNode(key, value)
                self.listOfMostRecent.setHeadTo(newNode)
                self.currentSize += 1
                self.cache[key] = newNode




class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node 

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return 
        self.tail = self.tail.prev
        self.tail.next = None
    
class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.nex = None


our_cache = LRU_Cache(5)
empty_cache = LRU_Cache(0)
negative_cache = LRU_Cache(-1)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# expect 1  
print(our_cache.get(1))
print() 
# expect 2 
print(our_cache.get(2))
print()
# expect -1 because 9 is not present in the cache
print(our_cache.get(9))

# adding 5 and 6 to our cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
"""returns -1 because the cache reached it's 
capacity and 3 was the least recently used entry"""  
print(our_cache.get(3))

# adding 1 to empty cache
empty_cache.set(1, 1)
# expect -1 because cache should be empty
print(empty_cache.get(1))

# adding 3 to negative cache
negative_cache.set(3, 3)
# expect -1 because cache has negative capacity
print(negative_cache.get(3))
  



