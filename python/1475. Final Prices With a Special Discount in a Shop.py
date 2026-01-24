class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=prices
        stack=[]
        for i in range(len(prices)):
            while stack and prices[i]<=res[stack[-1]]:
                x = stack.pop()
                res[x]-=prices[i]
            stack.append(i)
        return res
