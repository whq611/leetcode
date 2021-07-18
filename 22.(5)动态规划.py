class Solution:
    def generateParentthesis(self,n):
        total = []
        total.append([''])
        for i in range(1,n+1):
            l = []
            for j in range(i):
                list1 = total[j]
                list2 = total[i-1-j]
                for k1 in list1:
                    for k2 in list2:
                        el = '('+k1+')'+k2
                        l.append(el)
            total.append(l)
        return total[n]
        
        
