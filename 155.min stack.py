class MinStack:

    def __init__(self):
        self.a = []
        self.b = []


    def push(self, val: int) -> None:
        self.a.append(val)
        if not self.b or self.b[-1]>=val:
            self.b.append(val)
        


    def pop(self) -> None:
        tmp = self.a.pop()
        if self.b and self.b[-1]==tmp:
            self.b.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.b[-1]
