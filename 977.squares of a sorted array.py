from collections import deque
import math 
class Solution:
    def sortedSquares(self, nums):
        res = deque()
        l,r = 0,len(nums)-1
        while l <= r:
            if abs(nums[l])<abs(nums[r]):
                res.appendleft(int(math.pow(nums[r],2)))
                r -= 1
            else:
                res.appendleft(int(math.pow(nums[l],2)))
                l += 1
        return list(res)
