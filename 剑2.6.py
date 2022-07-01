class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i,j]
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
