class Solution:
    def firstUniqChar(self, s):
        if s == '':
            return ' '
        once = []
        duplicate = set()
        for i in s:
            if i in once:
                once.remove(i)
                dulplicate.add(i)
            if i not in dulplicate:
                once.append(i)
        if once == []:
            return ' '
        else:
            return once[0]
