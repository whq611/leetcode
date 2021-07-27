class Solution:
    def groupAnagrams(self, strs):
        ans = []
        j = 1
        ans.append([strs[0]])
        w = 0
        for i in strs[1:]:
            for k in range(j):
                if sorted(i) == sorted(ans[k][0]):
                    ans[k].append(i)
                    w = 0                   
                    break
                else:
                    w += 1
                    if w == j:
                        w = 0
                        ans.append([i])               
                        j += 1
                        
        return ans
