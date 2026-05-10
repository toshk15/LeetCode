class MyCalendarTwo:

    def __init__(self):
        self.over=[]
        self.noOver=[]
    def book(self, startTime: int, endTime: int) -> bool:
            for s,e in self.over:
                if endTime>s and e>startTime:
                    return False
            for s,e in self.noOver:
                if endTime>s and e>startTime:
                    self.over.append((max(startTime,s),min(e,endTime)))
            self.noOver.append((startTime,endTime))
            return True
        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
