class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heap=[-n for n in nums]
        heapq.heapify(heap)
        n=len(nums)

        for i in range(1, n, 2):
            nums[i]=-heapq.heappop(heap)
        for i in range(0, n, 2):
            nums[i]=-heapq.heappop(heap)
        return nums
