def largestOddNum(numStr):

    for i in range(len(numStr) - 1, -1, -1):
        if int(numStr[i]) % 2:
            return numStr[:i + 1]
    return ""
numStr = "234564"

print(largestOddNum(numStr))


"""
Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
"""