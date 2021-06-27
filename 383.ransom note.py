class Solution:
    def canConstruct(self, ransomNote, magazine):
        if not ransomNote:
            return True
        if len(ransomNote) > len(magazine):
            return False
        for i in range(len(ransomNote)):
            if magazine.find(ransomNote[i]) != -1:
                magazine = magazine.replace(ransomNote[i],'',1)
            else:
                return False
        return True
