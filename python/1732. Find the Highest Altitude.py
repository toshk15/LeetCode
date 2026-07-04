class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt=0
        s=0
        for n in gain:
            s+=n
            if s>max_alt:
                max_alt=s
        return max_alt
            
