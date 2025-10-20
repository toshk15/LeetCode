def minimumMoves(s):
    n=0
    c=0
    if "X" not in s:
        return 0
            
    while n<len(s):
        if s[n]=="O":
            n+=1
        else:
            c+=1
            n+=3
    return c


"""
Example 1:

Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO
We select all the 3 characters and convert them in one move.

Example 2:

Input: s = "XXOX"
Output: 2
Explanation: XXOX -> OOOX -> OOOO
We select the first 3 characters in the first move, and convert them to 'O'.
Then we select the last 3 characters and convert them so that the final string contains all 'O's.

Example 3:

Input: s = "OOOO"
Output: 0
Explanation: There are no 'X's in s to convert.
"""