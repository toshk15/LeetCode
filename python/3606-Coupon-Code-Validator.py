class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        priority={"electronics":0, "grocery": 1, "pharmacy":2, "restaurant":3}
        res=[]
        for c,b,act in zip(code, businessLine, isActive):
            if not act:
                continue
            if b not in priority:
                continue
            if not c:
                continue
            valid_code=True
            for ch in c:
                if not (ch.isalnum() or ch=='_'):
                    valid_code=False
                    break

            if valid_code:
                res.append((b,c))
            
        res.sort(key=lambda x:(priority[x[0]],x[1]))
        return [x[1] for x in res]
    
"""
 Example 1:

Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

Output: ["PHARMA5","SAVE20"]

Explanation:

    First coupon is valid.
    Second coupon has empty code (invalid).
    Third coupon is valid.
    Fourth coupon has special character @ (invalid).

Example 2:

Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

Output: ["ELECTRONICS_50"]

Explanation:

    First coupon is inactive (invalid).
    Second coupon is valid.
    Third coupon has invalid business line (invalid).

"""