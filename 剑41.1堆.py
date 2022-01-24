from heapq import *
class MedianFinder:
    def __init__(self):
        self.A = []
        self.B = []
    def addNum(self,num):
        if len(self.A) != len(self.B):
            heappush(self.A,num)
            heappush(self.B,-heappop(self.A))
        else:
            heappush(self.B,-num)
            heappush(self.A,-heappop(self.B))
    def findMedian(self):
        if len(self.A) != len(self.B):
            return self.A[0]
        else:
            return (self.A[0] - self.B[0]) / 2.0
