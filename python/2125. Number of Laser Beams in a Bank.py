class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        first=bank[0].count("1")
        res=0
        for n in range(1,len(bank)):
            second=bank[n].count("1")
            res+=(first*second)
            if second:
                first=second
        return res
        
