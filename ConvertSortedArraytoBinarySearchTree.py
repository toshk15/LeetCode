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