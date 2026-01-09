class Solution:
    def averageValue(self, nums: List[int]) -> int:
        a=0
        s=0
        for n in nums:
            if n%2==0 and n%3==0:
                s+=n
                a+=1
                print(s)
                print(a)
        return 0 if a==0 else int(s/a)
                
                
