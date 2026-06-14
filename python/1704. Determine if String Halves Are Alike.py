class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sv ={"a","e","i","o","u","A","E","I","O","U"}
        l=0
        r=len(s)-1
        lv=0
        rv=0
        while l<r:
            if s[l] in sv:
                lv+=1
            if s[r] in sv:
                rv+=1
            l+=1
            r-=1
        return lv==rv
