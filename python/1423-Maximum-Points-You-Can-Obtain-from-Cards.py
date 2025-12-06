"""
def maxScore(cardPoints, k):
    leftSum = sum(cardPoints[:k])        
    rightSum = 0
    leftSumSub = 0
    maximum = 0
    sumLeftRight = 0
    res = 0
        
    if len(cardPoints)==k:
        return leftSum

    for i in range(1, k+1):
        rightSum = sum(cardPoints[-i:])
        leftSumSub += cardPoints[k-i]
        sumLeftRight = leftSum - leftSumSub
        res = sumLeftRight + rightSum
        maximum = max(maximum, res, leftSum)
    return maximum
    """
def maxScore(cardPoints, k):
    leftSum = sum(cardPoints[:k])
    res = maximum = leftSum       

    if len(cardPoints)==k:
        return leftSum

    for i in range(1, k+1):
        res+= cardPoints[-i]-cardPoints[k-i]
        maximum = max(res, maximum)
         
    return maximum

nums = [1,2,3,4,5,6,1]
print(maxScore(nums,3))



"""
Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
"""
        