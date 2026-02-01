class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ope=0

        while True:
            isSorted=True
            aux=sorted(nums)
            if aux!=nums:
                isSorted=False

            if isSorted:
                return ope
            minSum=float("inf")
            idx=-1

            for i in range(len(nums)-1):
                currSum=nums[i]+nums[i+1]
                if currSum < minSum:
                    minSum=currSum
                    idx=i
            res=[]
            res=nums[:idx]
            res.append(minSum)
            res.extend(nums[idx+2:])
            nums=res
            ope+=1
        return ope
                    
