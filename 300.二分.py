import bisect
class Solution:
    def lengthOfLIS(self, nums):
        sub = []
        for num in nums:
            i = bisect_left(sub,num)
            if i == len(sub):
                sub.append(sum)
            else:
                sub[i] = num
        return len(sub)
