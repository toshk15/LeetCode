def rearrangeArray(self, nums: List[int]) -> List[int]:
    pos=[]
    neg=[]

    for i in nums:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
   
    i,j,k = 0,0,0
    while i < len(pos) and j<len(neg):
        nums[k]=pos[i]
        k+=1
        nums[k]=neg[j]
        k+=1
        i+=1
        j+=1

    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num 
                neg += 2
        
        return ans
    """
    return nums
