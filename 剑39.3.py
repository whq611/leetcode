import random
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice()
            sume = 0
            for elem in nums:
                if elem == candidate:
                    sume += 1
            if sume>majority_count:
                return candidate
