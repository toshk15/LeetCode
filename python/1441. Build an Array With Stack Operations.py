class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        stack=[]
        for r in range(1,n+1):
            res.append(r)
            stack.append("Push")
            if r not in target:
                res.pop()
                stack.append("Pop")
            if res==target:
                break
        return stack
            
            
            
