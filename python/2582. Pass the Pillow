class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        inc=1
        dir=1
        for i in range(time):
            inc+=dir
            if inc==1 or inc==n:
                dir*=-1
        return inc
