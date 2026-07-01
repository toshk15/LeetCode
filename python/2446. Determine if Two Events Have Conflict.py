class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1,e1=event1
        s2,e2=event2
        return not(e1<s2 or e2<s1)
