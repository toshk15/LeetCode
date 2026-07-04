class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res=0
        for n in hours:
            if n>=target:
                res+=1
        return res
