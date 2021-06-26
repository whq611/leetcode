class Solution:
    def lengthOfLastWord(self, s):
         a = s.split()
         for i in a[::-1]:
             if i != '':
                 return len(i)
         return 0
 
