class Solution:
    def isPalindrome(self, s):
        sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
