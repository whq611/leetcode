class Solution:
    def minArray(self, numbers):
        if len(numbers) == 1:
            return numbers[0]
        i,j = 0,1
        while j < len(numbers):
            if numbers[j] < numbers[i]:
                return numbers[j]
            i += 1
            j += 1
        return numbers[0]
