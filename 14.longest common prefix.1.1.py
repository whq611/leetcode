
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            if any(i == len(strs[j]) or strs[0][i] != strs[j][i] for j in range(1,count)):
                   return strs[0][:i]
        return strs[0]
            
                   
                
        
        
