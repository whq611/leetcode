import itertools
class Solution:
    def addOperators(self,num,target):
        ans = []
        for comb in itertools.product(['+','-','*',''],repeat=len(num)-1):
            s = sum[0]
            vals = [num[0]]
            for char,val in zip(comb,num[1:]):
                s += char + val
                if char == '':
                    vals[-1] += val
                else:
                    vals.append(val)
            for val in vals:
                if val[0] == '0' and len(val)>1:
                    break
                else:
                    if eval(s) == target:
                        ans.append(s)
        return ans
                    
