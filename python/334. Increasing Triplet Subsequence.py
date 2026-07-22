class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a=float("inf")
        b=float("inf")
        for n in nums:
            if n<a:
                a=n
            elif a<n<b:
                b=n
            elif n>b:
                return True
        return False
