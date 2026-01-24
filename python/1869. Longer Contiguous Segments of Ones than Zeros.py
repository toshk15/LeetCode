class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros=0
        ones=0
        maxone=0
        maxzero=0
        for n in s:
            if n=="1":
                zeros=0
                ones+=1
                maxone=max(maxone,ones)
            else:
                ones=0
                zeros+=1
                maxzero=max(maxzero,zeros)
        return True if maxone>maxzero else False
            
