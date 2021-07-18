class Solution:
    def generateParentthesis(self,n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParentthesis(c):
                for right in self.generateParentthesis(n-1-c):
                    ans.append('({}){}'.format(left,right))
        return ans
