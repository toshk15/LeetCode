class Solution:
    def modifyString(self, s: str) -> str:
        sn="abc"
        sl = list(s)
        for i in range(len(s)):
            if sl[i] == "?":
                for ch in sn:
                    if (i>0 and sl[i-1]==ch) or (i+1<len(s) and sl[i+1]==ch):
                        continue
                    sl[i]=ch
                    break
        return "".join(sl)


"""
Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

"""