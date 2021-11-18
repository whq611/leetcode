class SparseVector:
    def __init__(self,nums):
        self.nums = nums
    def dotProduct(self,vec):
        a = len(self.nums)
        result = 0
        for i in range(a):
            result += self.nums[i] * vec.nums[i]
        return result
