class RandomizedSet:

    def __init__(self):
        self.list=[]
        self.dict={}        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val]=len(self.list)-1  
        return True      

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        lastValList = self.list[-1]
        indexValDel = self.dict[val]
        self.list[indexValDel]=lastValList
        self.dict[lastValList]=indexValDel
        self.list.pop()
        del self.dict[val]
        return True        

    def getRandom(self) -> int:
        return random.choice(self.list)

"""
Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""


    


