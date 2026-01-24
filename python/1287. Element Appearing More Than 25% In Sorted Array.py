class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        c=Counter(arr)
        percent = int((n/100)*25)
        print(percent)
        for i,j in c.items():
            print(i)
            if j>percent:
                return i
