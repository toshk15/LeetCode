class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table =[None] * size

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index+1)%self.size
            if index == start_index:
                break
        return None
    
    def delete(self, key):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] ==  key:
                self.table[index] = None
                return
            index = (index+1)%self.size
            if index == start_index:
                break

    

ha = HashTableLinearProbing(10)
ha.insert(10, 1)
ha.insert(10, 10)
ha.insert(20, 10)
ha.delete(20)

print(ha.search(20))
        