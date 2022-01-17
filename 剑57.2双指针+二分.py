class Solution:
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target: 
                m = (i+j)//2
                if nums[i] + nums[m] > target:
                    j = m - 1
                elif nums[i] + nums[m] < target:
                    j -= 1
                else:
                    return nums[i], nums[m]
            elif s < target: 
                m = (i+j)//2
                if nums[j] + nums[m] > target:
                    i += 1
                elif nums[j] + nums[m] < target:
                    i = m + 1
                else:
                    return nums[j], nums[m]
            else: return nums[i], nums[j]
        return []
