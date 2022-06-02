class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        else:
            return self.stack_in[0]
    def empty(self) -> bool:
        return not(self.stack_in or self.stack_out)
