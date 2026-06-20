class NumArray:

    def __init__(self, nums: List[int]):
       self.arr=[]
       s=0
       for n in nums:
          s+=n
          self.arr.append(s)
        

    def sumRange(self, left: int, right: int) -> int:
       r=self.arr[right]
       l=self.arr[left-1] if left>0 else 0
       return r-l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
