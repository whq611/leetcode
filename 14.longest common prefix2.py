class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ''
        prefix,count = strs[0],len(strs)
        for i in range(1,count):
            prefix = self.compare(prefix,strs[i])
            if not prefix:
                break
        return prefix

    def compare(self,str1,str2):
        length = min(len(str1),len(str2))
        for each in range(length):
            if str1[each] != str2[each]:
                return str1[:each]
        return str1[:length]
                
