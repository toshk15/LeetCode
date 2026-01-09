class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        c=0
        curr_min=int(current[:2])*60+int(current[3:])
        corr_min=int(correct[:2])*60+int(correct[3:])
        diff=corr_min-curr_min
        intervals=[60,15,5,1]
        for s in intervals:
            c+=diff//s
            diff%=s
            if diff==0:
                break
        return c
        
        
