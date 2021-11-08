class Solution:
    def search(self, nums, target):
        a = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                b = m
                a += 1
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if l > r:
            return 0
        c = b
        while c+1 < len(nums) and nums[c+1] == target:
            a += 1
            c += 1
        while b-1>= 0 and nums[b-1] == target:
            a += 1
            b -= 1
        return a
