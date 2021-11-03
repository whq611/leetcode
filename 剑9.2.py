from collections import deque
class CQueue:
    def __init__(self):
        self.A = deque()

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if not self.A:
            return -1
        return self.A.popleft()
