class Solution:
    def findBuildings(self, heights):
        result = [0]
        for i in range(1,len(heights)):
            while result and heights[i] >= heights[result[-1]]:
                result.pop()
            result.append(i)
        return result
