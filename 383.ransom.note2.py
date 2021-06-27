class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        for i in ransomNote:
            if magazine.find(i) != -1:
                magazine = magazine.replace(i,'',1)
            else:
                return False
        return True
