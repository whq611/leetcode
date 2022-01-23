class Solution:
    def isStraight(self, nums):
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                joke += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[4]-nums[joker]<5
