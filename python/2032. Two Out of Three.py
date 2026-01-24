class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res=set()
        n1=set(nums1)
        n2=set(nums2)
        n3=set(nums3)
        s1=n1&n2 
        s2=n1&n3
        s3=n2&n3
        res=s1.union(s2,s3)
        return list(res)
        
