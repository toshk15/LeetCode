def largestOddNum(numStr):

    for i in range(len(numStr) - 1, -1, -1):
        if int(numStr[i]) % 2:
            return numStr[:i + 1]
    return ""
numStr = "234564"

print(largestOddNum(numStr))

        