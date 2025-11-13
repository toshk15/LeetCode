def plusOne(digits):
    """
    s=""
    res=[]
    for i in digits:
        s+=str(i)
    s = int(s)
    s+=1
    s = str(s)

    for i in s:
        res.append(int(i))
        
    return res

    """

    n = len(digits)

    for i in range(n-1, -1, -1):
        digits[i]+=1
        digits[i]%=10
        if digits[i]!=0:
            return digits
    return [1] + digits

digits=[1,9,9]
print(plusOne(digits))


"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""