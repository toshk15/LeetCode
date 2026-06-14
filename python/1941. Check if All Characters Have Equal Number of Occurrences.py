class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        seen=set()
        c=Counter(s)
        for k,v in c.items():
            if c[k] not in seen:
                seen.add(v)
        return len(seen)==1
        
        
