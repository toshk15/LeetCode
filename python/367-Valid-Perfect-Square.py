"""
def isPerfect(num):

    for i in range(1, num+1):
        if i*i == num:
            return True
        if i*i > num:
            return False

"""       
def isPerfect(num):

    l, r = 0, num

    while l <= r:
        mid = (l+r)//2
        if mid*mid > num:
            r = mid - 1
        elif mid * mid < num:
            l = mid + 1
        else:
            return True
    return False

x = 64
print(isPerfect(x))

"""
Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

"""