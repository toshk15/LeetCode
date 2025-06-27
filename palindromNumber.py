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

        