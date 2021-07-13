class Solution:
    def increasingTriplet(self, nums):
        a = len(nums)
        for i in range(a-2):
            for j in range(i+1,a-1):
                if nums[i] < nums[j]:
                    for k in range(j+1,a):
                        if nums[j] < nums[k]:
                            return True
        return False
