"""
class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class Hashmap:
    def __init__(self):
        self.map = [Node() for i in range(1000)]
        #print(list(self.map))

    def hashIndex(self, key):
        return key % len(self.map)
    
    def put(self, key, value):
        curr = self.map[self.hashIndex(key)]
        #print(curr)
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key,value)

    def get(self, key):
        curr = self.map[self.hashIndex(key)].next
        while curr and curr.key != key:
            curr = curr.next
        if curr:
            return curr.val
        return -1
    
    def remove(self, key):
        curr = self.map[self.hashIndex(key)]
        while curr.next and curr.next.key != key:
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next

"""

class NodeList:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class Hashmap:
    def __init__(self):
        self.map = [NodeList() for i in range(1000)]
    

    def indexNode(self, key):
        return key % (len(self.map))
    
    def put(self, key, value):
        curr = self.map[self.indexNode(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = NodeList(key, value)

    def get(self, key):
        curr = self.map[(self.indexNode(key))]
        curr = curr.next

        while curr and curr.key != key:
            curr = curr.next
        if curr:
            return curr.val
        else:
            return -1
    
    def remove(self, key):

        curr = self.map[(self.indexNode(key))]
        
        
        while curr.next and curr.next.key != key:
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next    

        
    
h = Hashmap()
h.put(1, 3)
h.put(2, 4)
h.put(1001, 1)
h.put(1001, 5)
h.put(1002, 10)
print(h.get(1001))
print(h.get(1002))
print(h.get(2))
h.remove(1)
print(h.get(1))
