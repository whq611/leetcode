class Solution:
    def validPalindrome(s):
        left,right = 0,len(s)-1
        while left<right:
            if s[left] != s[right]:
                if s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]:
                    return True
                else:
                    return False
            left += 1
            right += 1
        return True
                
    
