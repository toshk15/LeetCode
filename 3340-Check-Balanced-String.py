class Solution:
    def isBalanced(self, num: str) -> bool:
        sumOdd=[]
        sumEven=[]

        for n in range(len(num)):
            if n%2==0:
                sumEven.append(int(num[n]))
            else:
                sumOdd.append(int(num[n]))
        return sum(sumEven)==sum(sumOdd)

"""
Example 1:

Input: num = "1234"

Output: false

Explanation:

    The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
    Since 4 is not equal to 6, num is not balanced.

Example 2:

Input: num = "24123"

Output: true

Explanation:

    The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
    Since both are equal the num is balanced.

"""