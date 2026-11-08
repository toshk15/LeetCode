class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c=Counter(s)
        d=defaultdict(list)
        for ch,num in c.items():
            d[num].append(ch)
        res=[]
        large=0
        for num,ch in d.items():
            if len(ch)>len(res) or len(ch)==len(res) and num>large:
                large =num
                res=ch
        return ''.join(res)

            
            
