class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = [0] * 32
        res = 0
        for num in nums:
            for i in range(32):
                a[31-i] += ((num>>i)&1)
        for i in range(32):

            res<<=1
            res |= a[i]%3
            
        return res if a[0] % 3 == 0 else ~(res ^ 0xffffffff)
