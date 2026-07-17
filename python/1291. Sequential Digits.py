class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        q=deque(range(1,10))
        while q:
            n=q.popleft()
            if n>high:
                continue
            if low<=n<=high:
                res.append(n)
            x=n%10
            if x<9:
                n=n*10+(x+1)
                q.append(n)
        return res
        
