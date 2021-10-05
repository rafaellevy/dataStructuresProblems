class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # create an empty set
    union_set = set()
    # start at head of linked list 1
    cur_node = llist_1.head
    # go through linked list
    while cur_node:
        # add value of current node to set
        union_set.add(cur_node.value)
        cur_node = cur_node.next
    # start at head of linked list 2
    cur_node = llist_2.head
    while cur_node:
        union_set.add(cur_node.value)
        cur_node = cur_node.next
    
    # set has all the union values now, so we create a new linked list.
    union_llist = LinkedList()
    for value in union_set:
        union_llist.append(value)
    return union_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    # create first set
    inter_set1 = set()
    # set pointer/cur_node at head of first linked list
    cur_node = llist_1.head
    # go through first linked list
    while cur_node:
        inter_set1.add(cur_node.value)
        cur_node = cur_node.next
    # create second set
    inter_set2 = set()
    # set cur_node at head of second linked list
    cur_node = llist_2.head
    while cur_node:
        inter_set2.add(cur_node.value)
        cur_node = cur_node.next
    # find intersection of two sets
    inter_set = inter_set1.intersection(inter_set2)

    # using that intersection set, make the intersection linked list
    inter_llist = LinkedList()
    for value in inter_set:
        inter_llist.append(value)

    return inter_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))