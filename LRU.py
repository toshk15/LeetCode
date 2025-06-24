class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        #left=lru, right = most recent
        self.left , self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left   

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
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
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def print(self):
        curr = self.left
        while curr:
            print(curr.val)
            curr = curr.next
    



c = LRUCache(2)
#c.print()
c.put(1,1)
c.put(2,2)
#c.print()
print(c.get(1))
c.put(3,3)
print(c.get(2))
        