class Solution:
    def Kclosest(self,points,k):
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:k]
