class Solution:
    def reverseVowels(self, s):
        x = 'aeiouAEIOU'
        res=[]
        j=len(s)-1
        for i in s:
            if i in x:                      
                while s[j] not in x:
                    j-=1
                res.append(s[j])
                j-=1
            else:
                res.append(i)
        return ''.join(res)
