class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {"type":0, "color":1, "name":2}
        c=0
        idx = d[ruleKey]
        for x in items:
            if x[idx]==ruleValue:
                c+=1
        return c
            
