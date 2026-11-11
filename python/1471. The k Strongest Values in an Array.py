class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        n=len(arr)
        res=[]
        ans=[]
        arr.sort()
        m=arr[(n-1)//2]
        for n in arr:
            res.append((abs(n - m),n))
        res.sort(reverse="True")
        for i in range(k):
            ans.append(res[i][1])
        return ans
        
         
