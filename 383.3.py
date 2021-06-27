class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(ransomNote)
        b = list(magazine)
        
        try:
            for i in a:
                b.remove(i)
            return True
        except:
            return False
