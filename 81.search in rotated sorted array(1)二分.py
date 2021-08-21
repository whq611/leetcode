class Solution:
    def search(self,nums,target):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            while l < m and nums[l] == nums[m]:
                l += 1
            while r > m and nums[r] == nums[m]:
                r -= 1
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
