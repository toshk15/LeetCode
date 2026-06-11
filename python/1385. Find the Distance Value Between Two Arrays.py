class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        c=0
        for n in arr1:
            f=0
            for nn in arr2:
                f+=1
                if abs(nn-n)<=d:
                    break
                if f==len(arr2):
                    c+=1
        return c
