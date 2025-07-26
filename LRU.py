"""
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        #left=lru, right = most recent
        self.head , self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head   

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #remove from the list and delete the lru from the hash
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
"""

class DoublyLinkList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None
    

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyLinkList(-1,-1)
        self.tail = DoublyLinkList(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.remove_node(self.cache[key])
        self.add_to_tail(self.cache[key])
        return self.cache[key].val
    
    def put(self, key, value):
        if key in self.cache:
            self.remove_node(self.cache[key])
        node = DoublyLinkList(key, value)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.head.next.val]
            self.remove_node(self.head.next)
        self.add_to_tail(node)
    
    def add_to_tail(self, node):
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
c = LRUCache(2)
#c.print()
c.put(1,1)
c.put(2,2)
c.put(1,1)
#c.print()
print(c.get(1))
c.put(3,3)
print(c.get(2))
        