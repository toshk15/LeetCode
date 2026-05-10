class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c=Counter(str(n))
        for i in range(30):
            i=2**i
            p=Counter(str(i))
            if p==c:
                return True
        return False
