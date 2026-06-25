class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        v=0
        d=defaultdict(int)
        n=str(n)
        for c in n:
            d[c]+=1
        print(d)
        min_val=min(d.values())
        all_min_keys = [k for k, v in d.items() if v == min_val]
        return int(min(all_min_keys))
