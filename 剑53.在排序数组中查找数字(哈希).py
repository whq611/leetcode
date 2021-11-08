class Solution:
    def search(self, nums, target):
        a = {}
        a[target] = 0
        for i in nums:
            if i == target:
                a[target] += 1
        return a[target]
