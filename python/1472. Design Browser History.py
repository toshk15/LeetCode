class BrowserHistory:

    def __init__(self, homepage: str):
        self.backh=[homepage]
        self.fronth=[]
        
    def visit(self, url: str) -> None:
        self.backh.append(url)
        self.fronth=[]
        
    def back(self, steps: int) -> str:
        while steps and len(self.backh)>1:
            self.fronth.append(self.backh.pop())
            steps-=1
        return self.backh[-1]
        

    def forward(self, steps: int) -> str:
        while steps and self.fronth:
            self.backh.append(self.fronth.pop())
            steps-=1
        return self.backh[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
#obj = BrowserHistory(homepage)
#obj.visit(url)
#param_2 = obj.back(steps)
#param_3 = obj.forward(steps)
