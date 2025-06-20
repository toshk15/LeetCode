import random

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.idx_map = {}

    def insert(self, val):
        if val in self.idx_map:
            return False
        
        self.data.append(val)
        self.idx_map[val] = len(self.data) - 1
        return True
    
    def delete(self, val):
        if val not in self.idx_map:
            return False
        
        last_element = self.data[-1]
        idx_to_remove = self.idx_map[val]
        self.data[idx_to_remove] = last_element
        self.idx_map[last_element] = idx_to_remove
        self.data.pop()
        del self.idx_map[val]
        return True
    
    def get_random(self):
        return random.choice(self.data)
    
    def print(self):
        print(self.data)
        print(self.idx_map)

n = RandomizedSet()
n.insert(1)
n.insert(2)
n.insert(2)
n.insert(3)
n.delete(3)
n.delete(2)
n.print()
    


    


