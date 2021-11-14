class Solution:
    def twoSum(self, numbers, target):
        a = dict()
        for i,num in enumerate(numbers):
            if (target-num) in a:
                return [a[target-num]+1,i+1]
            a[num] = i
        return[]
