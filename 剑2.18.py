class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s:
            if i.isdigit(): a.append(i)
            elif i.isalpha(): a.append(i.lower())
        return a==a[::-1]
