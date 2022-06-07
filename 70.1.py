class Solution:
    def climbStairs(self, n: int) -> int:
        slow, fast = 1,1
        while(n>0):
            slow, fast = fast, slow+fast
            n-=1
        return slow
