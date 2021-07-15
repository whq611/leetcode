class Solution:
    def increasingTriplet(self,nums):
        one = two = float('inf')
        for three in nums:
            if three > two:
                return True
            elif three<=one:
                one = three
            else:
                two = three
        return False
