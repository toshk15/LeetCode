def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    l=0
    r=len(nums)-1
    def convert(l,r):
        if l>r:
            return None
        m=(l+r)//2
        root = TreeNode(nums[m])
        root.left=convert(l,m-1)
        root.right=convert(m+1,r)
        return root
    return convert(l,r)


"""
Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

"""