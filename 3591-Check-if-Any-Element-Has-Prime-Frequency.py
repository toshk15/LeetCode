class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isPrime(n):
            if n<2:
                return False

            for i in range(2, int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        
        c=Counter(nums)
        for i in c.values():
            if isPrime(i):
                return True
        return False
    
"""

Example 1:

Input: nums = [1,2,3,4,5,4]

Output: true

Explanation:

4 has a frequency of two, which is a prime number.

Example 2:

Input: nums = [1,2,3,4,5]

Output: false

Explanation:

All elements have a frequency of one.

Example 3:

Input: nums = [2,2,2,4,4]

Output: true

Explanation:

Both 2 and 4 have a prime frequency.

"""