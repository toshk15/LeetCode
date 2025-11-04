class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices=sorted(prices)
        x=prices[0]+prices[1]
        if money>=x:
            return money-x
        else:
            return money
        
"""
Example 1:

Input: prices = [1,2,2], money = 3
Output: 0
Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

Example 2:

Input: prices = [3,2,3], money = 3
Output: 3
Explanation: You cannot buy 2 chocolates without going in debt, so we return 3.
"""