# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)
        visited=set()
        def createGraph(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                createGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                createGraph(node.right)
        createGraph(root)    
        q=deque()
        visited.add(target.val)
        q.append(target.val)
        dist=0
        while q and dist<k:
            dist+=1
            for i in range(len(q)):
                node=q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        return list(q)
            
            
