def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for i in range(2, len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k


  def removeDuplicates(self, nums: List[int]) -> int:
        l,r =0,0
        n=len(nums)
        
        while r<n:
            c=1
            while r+1<n and nums[r]==nums[r+1]:
                r+=1
                c+=1
            for i in range(min(2,c)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l