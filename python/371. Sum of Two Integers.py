class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff
        max_val=0x7fffffff
        a=a & mask
        b=b & mask
        while b:
            carry=((a & b)<<1)&mask
            a=a^b
            b=carry
        if a > max_val:
            return ~(a^mask)
        else:
            return a
