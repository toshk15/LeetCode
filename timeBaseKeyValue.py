class TimeMap:
    def __init__(self):
        self.key_store = {}

    def set(self, key, value, timestamp):
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])
    
    def get(self, key, timestamp):
        res, values = "", self.key_store.get(key,[])
        l,r = 0, len(values)-1
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res
    

c = TimeMap()

c.set("foo", "dog", 1)
print(c.get("foo", 1))
print(c.get("foo", 3))
c.set("foo", "cat", 4)
print(c.get("foo", 6))


