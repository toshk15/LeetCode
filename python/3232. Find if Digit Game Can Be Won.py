class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        one=0
        two=0
        for n in nums:
            if len(str(n))==1:
                one+=n
            else:
                two+=n
        return one!=two
