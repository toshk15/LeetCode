class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lic={}
        for c in licensePlate.lower():
            if c.isalpha():
                lic[c]=lic.get(c,0)+1

        def contain(w):
            short={}
            for c in w.lower():
                short[c]=short.get(c,0)+1
            for c,lon in lic.items():
                if short.get(c,0)<lon:
                    return False
            return True

        shortword=""
        for w in words:
            if contain(w):
                if len(shortword)==0 or len(w)<len(shortword):
                    shortword=w
        return shortword
        
