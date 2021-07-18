class Solution:
    def generateParentthesis(self,n):
        if n == 1:
            return ['()']
        res = set()
        for i in self.generateParentthesis(n-1):
            for j in range(len(i)+2):
                res.add(i[0:j]+'()'+i[j:])
        return list(res)
