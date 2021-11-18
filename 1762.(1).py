class Solution:
    def findBuildings(self, heights):
        result = []
        max_height = -1
        for current in range(len(heights))[::-1]:
            if max_height < heights[current]:
                result.append(current)
                max_height = heights[current]
        return reversed(result)
