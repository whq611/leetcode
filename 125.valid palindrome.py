class Solution:
    def isPalindrome(self, s):
        s = ''.join(list(filter(str.isalnum, s)))
        s = s.lower()
        if s[::-1] == s:
            return True
        return False
