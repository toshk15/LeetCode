class Solution:
    def minimumChairs(self, s: str) -> int:
        per=0
        min_chair=0
        for i in s:
            if i=="E":
                per+=1
                min_chair=max(min_chair, per)
            else:
                per-=1
        return min_chair
