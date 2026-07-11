class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res=[0]*1001
        for trip in trips:
            passenger,start,end=trip
            res[start]+=passenger
            res[end]-=passenger
        total=0
        for i in range(len(res)):
            total+=res[i]
            if total>capacity:
                return False
        return True
