import bisect
import random
class Solution:
    def __init__(self,w):
        self.a = []
        t = sum(w)
        c = 0
        for x in w:
            c += x
            self.a.append(c / t)
    def pickIndex(self):
        return bisect.bisect_left(self.a,random.random())
