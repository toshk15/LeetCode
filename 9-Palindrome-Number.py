"""
def isPalindrome(x):
    if x < 0:
        return False
    
    div = 1
    while x>= 10 * div:
        div *= 10
    
    while x:
        right = x % 10
        left = x // div

        if left != right:
            return False
        
        x = (x % div) // 10
        div = div / 100

    return True
"""
def isPalindrome(num):
    strNum = str(num)
    #print(strNum)
    l, r = 0, len(strNum)-1
    while l <= r:
        if strNum[l] == strNum[r]:
            l += 1
            r -= 1
        return True
    return False  




x = 1234321
print(isPalindrome(x))

"""
 Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""       