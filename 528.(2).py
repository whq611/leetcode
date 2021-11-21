import random
class Solution:
    def __init__(self,w):
        self.presum = []
        self.total = sum(w)
        cur_pre_sum = 0
        for x in w:
            cur_pre_sum += x
            self.presum.append(cur_pre_sum)

    def pickIndex(self):
        target = self.tot_sum * random.random()
        for i,pre_sum in enumerate(self.presum):
            if target < pre_sum:
                return i
