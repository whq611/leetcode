class Solution:
    def majorityElement(self, nums):
        a = {}
        b = len(nums)/2
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
            if a[num] > b:
                return num
