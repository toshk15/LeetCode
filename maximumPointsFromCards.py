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
print(maxScore(nums))
        