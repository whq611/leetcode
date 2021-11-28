class Solution:
    def trap(self,height):
        ans = 0
        l,r = 0,len(height)-1
        lm = rm = 0
        while left<=right:
            lm = max(lm,height[l])
            rm = max(rm,height[r])
            if lm<rm:
                ans += lm - height[l]
                l += 1
            else:
                ans += rm - height[r]
                r -= 1
        return ans
            
