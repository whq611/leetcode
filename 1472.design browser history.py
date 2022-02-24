class BrowserHistory:
    def __init__(self,homepage):
        self.a = [homepage]
        self.i = 0
    def visit(self,url):
        del self.a[self.i+1:]
        self.a.append(url)
        self.i += 1
    def back(self,steps):
        self.i = max(0,self.i-steps)
        return self.a[self.i]
    def forward(self,steps):
        self.i = min(self.i+steps,len(self.a)-1)
        return self.a[self.i]
