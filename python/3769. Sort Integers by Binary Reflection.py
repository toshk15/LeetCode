class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflect(n):
            bs=""
            while n:
                bs=str(n%2)+bs
                n=n//2
            bs=bs[::-1]
            bs=int(bs,2)
            return bs
        res=[]
        sol=[]
        for n in nums:
            x=reflect(n)
            res.append([x,n])
        res.sort()
        for i,j in res:
            sol.append(j)
        return sol
