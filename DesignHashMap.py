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
class Node:
    def __init__(self,key=-1,val=-1):
        self.key=key
        self.val=val
        self.next=None

class MyHashMap:

    def __init__(self):
        self.size=1000
        self.map=[Node() for i in range(self.size)]
    
    def hash(self,key):
        return key%self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
       
        curr = self.map[index]
        while curr.next:
            if curr.next.key==key:
                curr.next.val = value
                return 
            curr=curr.next
        curr.next = Node(key,value)       
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr =  self.map[index]
        while curr:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr =  self.map[index]
        prev=None
        while curr and curr.key!=key:
            prev=curr
            curr=curr.next
        if curr==None:
            return -1
        if prev==None:
            self.map[index]=None
        else:
            prev.next=curr.next

 
"""
Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

"""