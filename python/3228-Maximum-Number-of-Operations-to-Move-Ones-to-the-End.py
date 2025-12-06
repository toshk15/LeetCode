class Solution:
    def maxOperations(self, s: str) -> int:
        cnt=0
        i=0
        res=0
        while i < len(s):
            if s[i]=="1":
                cnt+=1
                i+=1

            elif s[i]=="0":
                res+=cnt
                i+=1
                while i<len(s) and s[i]=="0":
                    i+=1
        return res


"""

Example 1:

Input: s = "1001101"

Output: 4

Explanation:

We can perform the following operations:

    Choose index i = 0. The resulting string is s = "0011101".
    Choose index i = 4. The resulting string is s = "0011011".
    Choose index i = 3. The resulting string is s = "0010111".
    Choose index i = 2. The resulting string is s = "0001111".

Example 2:

Input: s = "00111"

Output: 0

"""