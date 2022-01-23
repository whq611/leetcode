class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []


    def addNum(self, num):
        i = 0
        while i<len(self.a) and num>self.a[i]:
            i += 1
        self.a.insert(i,num)


    def findMedian(self):
        b = len(self.a)
        if b%2 == 1:
            return self.a[b//2]
        else:
            return (self.a[b//2] + self.a[b//2-1])/2
