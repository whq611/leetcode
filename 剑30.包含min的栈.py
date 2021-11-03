class MinStack:

    def __init__(self):
        self.a = []
        """
        initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.a.append(x)


    def pop(self) -> None:
        self.a.pop()


    def top(self) -> int:
        b = self.a.pop()
        self.a.append(b)
        return b


    def min(self) -> int:
        return min(self.a)
