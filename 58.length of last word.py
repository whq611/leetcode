class Solution:
    def lengthOfLastWord(self, s):
        s_list = s.split()
        if not s_list:
            return 0
        return len(s_list[len(s_list) - 1])
