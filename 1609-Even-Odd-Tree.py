# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:       
      
        q = deque([root])
        level=1
        
        while q:
            print(level)
            odd=float("-inf")     
            even=float("inf")
           
            for i in range(len(q)):
                node = q.popleft()
                if level%2==1:
                    if node.val%2==1 and node.val>odd:
                        odd=node.val
                    else:
                        return False
                elif level%2==0:
                    if node.val%2==0 and node.val<even:
                        even=node.val
                    else:
                        return False
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
                
        return True 
    
"""


Example 1:

Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:

Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:

Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

"""