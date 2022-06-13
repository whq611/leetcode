class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = dict()
        n = len(nums)//2
        for num in nums:
            if num in a:
                a[num]+=1
            else:
                a[num]=1
            if a[num]>n:
                return num
