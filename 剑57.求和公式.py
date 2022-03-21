class Solution:
    def findContinuousSequence(self, target):
        i,j,res = 1,2,[]
        while i<j:
            j = (-1 + (1+4*(2*target+i*i-i))**0.5)/2
            if i<j and j==int(j):
                res.append(list(range(i,int(j)+1)))
            i+=1
        return res
