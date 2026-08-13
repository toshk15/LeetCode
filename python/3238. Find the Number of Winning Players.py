class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d=defaultdict(int)
        win=set()
        for p in pick:
            d[tuple(p)]+=1
            if d[tuple(p)]>p[0]:
                win.add(p[0])
        return len(win)
